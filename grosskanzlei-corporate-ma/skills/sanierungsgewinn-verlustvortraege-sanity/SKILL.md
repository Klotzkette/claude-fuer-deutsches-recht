---
name: sanierungsgewinn-verlustvortraege-sanity
description: "Sanity-Check der Verlustvorträge im Distressed-Due-Diligence-Prozess. Modelliert den Verbrauch von körperschaft- und gewerbesteuerlichen Verlustvorträgen, Zinsvorträgen und EBITDA-Vorträgen durch einen prognostizierten Sanierungsertrag (§ 3a Abs. 3 EStG / § 7b GewStG). Liefert ein DD-Modul mit Verlustvortrag-Inventur, Verbrauchssimulation und Red-Flag-Liste für SPA-Verhandlung. Adressat ist das M&A-Team der Großkanzlei in Buy-side und Sell-side. Quellen Stand 06/2026."
---

# Sanierungsgewinn – Verlustvorträge Sanity im DD-Prozess

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Sanierungsgewinn – Verlustvorträge Sanity im DD-Prozess
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Worum geht es

Verlustvorträge sind in Distressed-Transaktionen kein Buchungsposten, sondern Verhandlungsmasse. § 3a Abs. 3 EStG ordnet ihren zwingenden Verbrauch durch den späteren Sanierungsertrag an. Wer im Due-Diligence-Bericht den Verlustvortrag mit dem Wert aus dem Steuerbescheid übernimmt, ohne den prognostizierten Verbrauch zu modellieren, liefert einen unbrauchbaren DD-Bericht.

Dieser Skill liefert das Modul, das dem Käufer und dem Sell-side-Team zeigt, **wie viel vom Verlustvortrag nach Restrukturierung tatsächlich übrig bleibt**.

## Wann dieses Modul hilft

- Buy-side-DD eines Targets mit erheblichen kumulierten Verlustvorträgen und absehbarem Sanierungsbedarf.
- Sell-side-DD bzw. Vendor-DD für einen Verkäufer, der mit dem Argument „Verlustvortrag = 200 Mio. EUR" in die Verhandlung geht.
- Restructuring-Beratung, in der die steuerliche Wirkung des Plans noch nicht modelliert ist.
- Konzern-Spin-offs oder Carve-outs mit gleichzeitigem Forderungsverzicht innerhalb des Konzerns.

Nicht dieser Skill ist primär, wenn lediglich eine Standard-Tax-DD ohne Sanierungsbezug gefragt ist; dann genügt das allgemeine M&A-DD-Modul. Hier geht es um den Sonderfall Sanierungsertrag.

## Rechtlicher Rahmen

- **§ 3a EStG** – Steuerbefreiung des Sanierungsertrags; setzt vier Voraussetzungen voraus: Sanierungsbedürftigkeit, Sanierungsfähigkeit, Sanierungseignung des Schulderlasses, Sanierungsabsicht der Gläubiger.
- **§ 3a Abs. 3 EStG** – die **zwingende Verrechnungsreihenfolge**: Sanierungsertrag verbraucht zunächst (i) den laufenden Verlust des Sanierungsjahres, (ii) verbleibende Verlustvorträge des Vorjahres, (iii) den verbleibenden Verlustvortrag, (iv) den Zinsvortrag nach § 4h EStG, (v) den EBITDA-Vortrag, (vi) Steuerpositionen weiterer Vorschriften. Erst danach greift die Steuerbefreiung auf einen etwaigen Rest.
- **§ 7b GewStG i. V. m. § 36 Abs. 2c GewStG** – gewerbesteuerliche Parallelregelung; gewerbesteuerliche Verlustvorträge werden separat verbraucht.
- **§ 8c KStG** – Anteilseignerwechsel über 50 % zerstört den Verlustvortrag im Grundsatz. Wird ein DD-Befund mit hohem Verlustvortrag dadurch entwertet, dass der Erwerbsvorgang selbst § 8c KStG auslöst? Dieses Spannungsfeld ist zwingend zu prüfen.
- **§ 8d KStG** – fortführungsgebundener Verlustvortrag als Rettungsanker; erfordert Antragstellung und strenge Fortführungsbindung.
- **§ 10d EStG** – Verlustvortrag mit Mindestbesteuerung; ab 1 Mio. EUR nur noch 60 % verrechenbar.
- **§ 4h EStG** – Zinsschranke; Zinsvortrag.

## / Schritt für Schritt

1. **Verlustvortrag-Inventur.** Steuerbescheide der letzten fünf Veranlagungszeiträume sichten, einschließlich Feststellungsbescheide nach § 10d EStG und nach § 10a GewStG. Achtung auf vorläufige Veranlagungen.
2. **Vortragsmappe vervollständigen.** Zinsvortrag § 4h EStG, EBITDA-Vortrag, ggf. verbleibende Steuerguthaben aus Organschaft. Zinsvortrag und EBITDA-Vortrag werden in der Praxis häufig vergessen.
3. **Sanierungsertrag prognostizieren.** Aus dem Sanierungsplan oder den geplanten Forderungsverzichten den voraussichtlichen Sanierungsertrag ermitteln. Schuldverzichte unter Besserungsschein gesondert behandeln.
4. **Verbrauchssimulation.** Drei Stufen modellieren: vor Steuern, nach Verbrauch der Vorträge, nach Anwendung § 3a EStG. Ergebnis ist eine Tabelle, die zeigt, was vom Verlustvortrag übrig bleibt.
5. **Mindestbesteuerung berücksichtigen.** § 10d EStG begrenzt die Verlustnutzung auf 1 Mio. EUR Sockelbetrag plus 60 % des darüber hinausgehenden Gewinns. Achtung: nach herrschender Auffassung gilt diese Begrenzung im Rahmen des § 3a Abs. 3 EStG nicht, weil der Sanierungsertrag dort verbraucht wird, bevor § 10d EStG eingreift. Dieser Punkt ist Streitfeld; im DD ausdrücklich als „streitig, Verlautbarung der Finanzverwaltung Stand 06/2026 zu prüfen" kennzeichnen.
6. **§ 8c KStG-Test.** Erwerb über 50 % der Anteile? Dann Verlustvortrag im Grundsatz untergegangen. Prüfen, ob § 8d KStG-Antrag möglich ist und ob die stille-Reserven-Klausel des § 8c Abs. 4 KStG greift.
7. **Disclosure-Red-Flags.** Verlustvorträge in Streit (Außenprüfung läuft, Einspruch gegen Feststellungsbescheid)? Verlustvortrag gefährdet durch Organschaft, Anteilseignerwechsel oder Strukturmaßnahmen?
8. **DD-Bericht-Modul schreiben.** Ergebnisdarstellung als Tabelle, Annahmen explizit, Quellen je Verlustvortrag-Position.

## Trade-off-Matrix

| DD-Stilfrage | Aggressive Sicht (Buy-side) | Konservative Sicht | Empfehlung Großkanzlei |
|---|---|---|---|
| Anwendbarkeit § 10d EStG-Begrenzung auf Sanierungsertrag | Begrenzung gilt nicht, voller Verbrauch | Begrenzung gilt, Sockelbetrag bleibt | Beide Szenarien rechnen |
| Sanierungseignung Schulderlass | Vereinbarung reicht | Wirtschaftliche Tragfähigkeit beweisen | Konservativ ansetzen |
| § 8d KStG Antrag | Sicherer Verlustvortrag-Schutz | Strenge Fortführungsbindung | Im DD als Option markieren |
| Verbindliche Auskunft | nicht erforderlich | unbedingt erforderlich | Erforderlich im Distressed-Deal |

## Praxistipps der alten Hasen

Erfahrene Tax-Partner schauen im Distressed-DD zuerst auf drei Zahlen: kumulierter Verlustvortrag laut letztem Feststellungsbescheid, prognostizierter Sanierungsertrag aus dem IDW-S6-Gutachten, und Differenz aus beidem. Der Rest ist Folge dieser Differenz. Drei weitere Beobachtungen aus der Praxis:

- **Der Zinsvortrag wird unterschätzt.** Bei einer fremdfinanzierten Holding kann der Zinsvortrag nach § 4h EStG im hohen siebenstelligen Bereich liegen und durch den Sanierungsertrag mitverzehrt werden.
- **Die Mindestbesteuerung-Frage ist Verhandlungsmasse.** Solange die Finanzverwaltung diese Frage nicht abschließend geklärt hat, lässt sich im SPA mit der Tax-Indemnity arbeiten.
- **Der Feststellungsbescheid ist oft nicht final.** Eine laufende Außenprüfung kann den Verlustvortrag noch deutlich verändern; diese Schwebephase gehört explizit in den DD-Bericht.

## SPA-/Plan-Klausel Mustertexte

**Vendor Warranty re Verlustvortrag (Auszug):**

> Verkäufergarantie Steuern: Der Verkäufer garantiert, dass die in Anlage X aufgeführten körperschaft- und gewerbesteuerlichen Verlustvorträge der Zielgesellschaft zum Stichtag in der dort genannten Höhe bestandskräftig festgestellt sind. Eine Garantie für den steuerlichen Bestand dieser Verlustvorträge nach Wirksamwerden der in diesem Vertrag vorgesehenen Sanierungsmaßnahmen wird nicht übernommen; insoweit verweisen die Parteien auf die Indemnity-Regelung gemäß Ziffer Y.

**Indemnity-Klausel zum Verbrauch durch Sanierungsertrag:**

> Tax Indemnity Sanierungsertrag: Der Verkäufer stellt den Käufer frei von steuerlichen Nachteilen, die daraus entstehen, dass die nach § 3a Abs. 3 EStG zwingende Verrechnungsreihenfolge zu einem höheren Verbrauch der Verlustvorträge führt als in dem Tax-Modell gemäß Anlage X angenommen, soweit der Abweichungsbetrag eine Schwelle von [Betrag] übersteigt.

## Typische Fehler in komplexer Transaktion

- Verlustvortrag mit dem Wert aus dem letzten Feststellungsbescheid übernommen, ohne die laufende Außenprüfung zu prüfen.
- Zinsvortrag § 4h EStG und EBITDA-Vortrag aus dem Sanity-Check vergessen.
- § 10d EStG-Mindestbesteuerung doppelt angewendet (in der Sanierungsmechanik und in der Verlustvortragsmodellierung), obwohl streitig ist, ob sie im Rahmen § 3a Abs. 3 EStG überhaupt greift.
- § 8c KStG-Test übersprungen, weil „nur 49,9 % erworben werden"; Hinzurechnungen von Stimmrechten oder nahestehenden Personen werden übersehen.
- DD-Bericht enthält keinen Hinweis auf die Notwendigkeit einer verbindlichen Auskunft nach § 89 AO.

## Querverweise

- Plugin `steuerrecht-anwalt-und-berater`: Skill zu § 8c und § 8d KStG; Skill zu § 89 AO.
- Plugin `insolvenzrecht`: Wirkung des Insolvenzplans auf Verlustvorträge.
- Plugin `grosskanzlei-corporate-ma`:
 - `grosskanzlei-corporate-ma-due-diligence-legal`
 - `gk-sanierungsgewinn-fruehe-mandantsteuerung-q-minus-zwoelf`
 - `gk-sanierungsgewinn-tax-warranty-und-tax-indemnity-im-spa`
 - `gk-sanierungsgewinn-stille-reserven-klausel-8c-iv-kstg`

## Quellen Stand 06/2026

- § 3a EStG; § 3a Abs. 3 EStG; § 7b GewStG i. V. m. § 36 Abs. 2c GewStG; § 8c KStG; § 8d KStG; § 10d EStG; § 4h EStG – jeweils aktuelle Fassung, prüfbar über gesetze-im-internet.de.
- BMF-Schreiben vom 27.04.2017 – Verifizierung im Bundessteuerblatt Stand 06/2026.
- FG Köln, Urteil vom 04.11.2025 – 12 K 1413/25 – prüfbar über dejure.org und NWB.
- FG Köln, Urteil vom 06.03.2012 – 13 K 3006/11, GmbHR 2012, 977 (vorgehend zu BFH I R 34/12) – verifizierte Fundstelle für die DD-Bewertung von Targets, die statt einer Sanierung in die Liquidation laufen (nachrangige Gesellschafterdarlehen, Erlöschen von Verbindlichkeiten und Verlustvorträgen mit Löschung).
- BFH (Großer Senat), Beschluss vom 28.11.2016 – GrS 1/15 – prüfbar über bundesfinanzhof.de.
- Sonstige BFH-Rspr. zu § 10d EStG und § 4h EStG als „ständige Rspr." formulieren; Verifizierung über bundesfinanzhof.de.

## V61 Deal-OS Boost

Dieser Skill arbeitet nicht passiv. Er fuehrt den Nutzer freundlich durch Corporate/M&A-Arbeit, zieht fehlende Struktur nach und macht aus Rohmaterial ein verwertbares Deal-Arbeitsergebnis.

- **Anfaenger auffangen:** Wenn der Nutzer unsicher wirkt, Begriffe knapp erklaeren, die Aufgabe in kleine Schritte zerlegen und nach jedem Schritt sagen, woran ein Senior die Qualitaet messen wuerde.
- **Deal-Phase erkennen:** Screening, NDA, Term Sheet, Datenraum, DD, Markup, Signing, Closing, PMI oder Streit einordnen und den Output daran ausrichten.
- **Padlet anbieten:** Bei chaotischen oder grossen Aufgaben ein Board mit Karten für Parteien, Dokumente, Risiken, Q&A, CPs, Gremien, Register, Owner und Fristen erzeugen.
- **Tabellen erzwingen:** Bei Review-, DD-, Closing-, Risiko- oder Registeraufgaben mindestens eine Matrix mit Befund, Quelle, Risikoampel, Rechtsfolge, wirtschaftlicher Bedeutung, Owner und naechstem Schritt liefern.
- **Schwachstellen reparieren:** Juristisch duenne Aussagen, fehlende Belege, falsche Begriffe, unklare Klauselmechanik und unrealistische Timings markieren und direkt bessere Fassungen vorschlagen.
- **Aktualitaetsdisziplin:** Bei Fusionskontrolle, FDI, FSR, Public M&A, UmwG/UmwStG, StaRUG/InsO, Steuer, Register und Aufsicht immer kenntlich machen, ob ein Live-Check der aktuellen Norm-/Behördenlage erforderlich ist.
- **Human-in-the-loop:** KI-Ergebnisse als Entwurf behandeln. Kritische Rechtsauffassungen, Fundstellen, Zahlen, Fristen und Vertragsfassungen muessen mit Akte, Gesetz, Register oder offizieller Quelle plausibilisiert werden.
- **Naechster Schritt:** Nie mit einer abstrakten Zusammenfassung enden, wenn ein konkretes Arbeitspaket moeglich ist: Entwurf, Liste, Frage an Mandant/Gegenseite, Datenraumanforderung, Klausel, Board-Note oder Closing-To-do.
