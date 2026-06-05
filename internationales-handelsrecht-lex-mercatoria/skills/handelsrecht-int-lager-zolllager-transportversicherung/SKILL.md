---
name: handelsrecht-int-lager-zolllager-transportversicherung
description: "INT Lager Zolllager Transportversicherung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# INT Lager Zolllager Transportversicherung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **INT Lager Zolllager Transportversicherung** im Plugin Internationales Handelsrecht Lex Mercatoria. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ihl-027-lager-und-zolllager` | Internationales Handelsrecht: Lagerrecht (HGB §§ 467-475h) und Zolllager nach Unionszollkodex (UZK) Art. 237-242. Lagerhalter-Pflichten, Haftung, Zollverfahren, Einfuhr- und Ausfuhrlager, ATLAS-Anmeldung und Zolllagertypen. |
| `ihl-028-transportversicherung` | Internationales Handelsrecht: Transportversicherung im internationalen Handel. Institute Cargo Clauses A/B/C (Lloyd's), All-Risk vs. benannte Gefahren, Versicherungspflicht nach Incoterms CIF/CIP, Versicherungszertifikat für Akkreditive und Subrogation. |
| `ihl-029-warentransit-und-gefahruebergang` | Internationales Handelsrecht: Gefahrübergang bei auf Reise befindlicher Ware nach CISG Art. 68 und Incoterms 2020. Verkauf auf Reise (string trading), Rückwirkungsfiktion, Dokumentengefahr und Absicherung durch Transportversicherung. |
| `ihl-030-zolltarif-und-ursprung` | Internationales Handelsrecht: Zolltarif (EU Kombinierte Nomenklatur, HS-Code) und nicht-präferenzieller Ursprung nach UZK Art. 59-63. Einreihung von Waren, wesentliche Be- und Verarbeitung, ursprungsbestimmende Vorgänge und Antidumping-Relevanz. |

## Arbeitsweg

Im Plugin Internationales Handelsrecht Lex Mercatoria gilt für **INT Lager Zolllager Transportversicherung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ihl-027-lager-und-zolllager`

**Fokus:** Internationales Handelsrecht: Lagerrecht (HGB §§ 467-475h) und Zolllager nach Unionszollkodex (UZK) Art. 237-242. Lagerhalter-Pflichten, Haftung, Zollverfahren, Einfuhr- und Ausfuhrlager, ATLAS-Anmeldung und Zolllagertypen.

# Lager- und Zolllager

## Worum es geht

Das Lagerrecht (HGB §§ 467-475h) regelt die Verwahrung von Waren durch einen gewerblichen Lagerhalter. Zolllager nach UZK Art. 237-242 erlauben Lagerung nicht-unionszollrechtlicher Waren ohne sofortige Zollschuldentstehung — wichtig für Transithandel und Bonded Warehouse.

## Kernnormen / Kernquellen

- **HGB § 467**: Lagervertrag — Pflicht zur Verwahrung
- **HGB § 471**: Lagerhalter-Haftung — Sorgfalt eines ordentlichen Kaufmanns
- **HGB § 475g**: Pfandrecht des Lagerhalters
- **UZK Art. 237**: Zolllager — Lagerung nicht-unionszollrechtlicher Waren
- **UZK Art. 240**: Typen (öffentliches/privates Zolllager Typ I-VI)
- **ATLAS**: Zollsystem der deutschen Zollbehörden (Bundeszollverwaltung)

## Schlüsselbegriffe

- Ordentlicher-Kaufmann-Maßstab: Haftungsstandard des Lagerhalters
- Lagerhalter-Pfandrecht: sichert Forderungen des Lagerhalters
- Zolllager Typ I/II: öffentliches Lager für jedermann (Typ I) oder bestimmten Nutzer (Typ II)
- Bonded Warehouse: nicht-unionszollrechtliche Ware ohne Zollschuld gelagert
- Wareneingangsprüfung: Dokumentation bei Übernahme für spätere Haftungsabgrenzung

## Typische Streitfragen / Anwendungsfälle

1. Lagerschäden durch Fehler des Lagerhalters: Haftungsgrenze HGB oder ADSp?
2. Zolllager: Kann Ware bearbeitet werden (veredelt, verarbeitet) ohne Zollschuldentstehung?
3. Pfandrecht Lagerhalter: Übertrifft es andere Sicherheiten (Eigentumsvorbehalte)?
4. Zolllager nach Brexit: Wie ändert sich die Behandlung UK-Waren in EU-Zolllager?
5. ATLAS-Anmeldung: Welche Pflichten hat der Lagerhalter bei Fehlern in der Warenbeschreibung?

## Methodik

- Lagervertrag: Einlagerungsdokumentation (Lagerhauptbuch) sorgfältig führen
- Zolllager: Bewilligung beim Hauptzollamt beantragen; laufende Bestandsführung UZK Art. 214
- Haftungsabgrenzung: Übernahmezustand dokumentieren (Fotos, Wiegung)
- Pfandrecht: Rangfolge mit anderen Sicherungsrechten im Vorfeld klären

## Output

- Lager- vs. Zolllager Unterscheidungsmatrix
- Zolllager-Bewilligungsvoraussetzungen (UZK Art. 237-242)
- Muster-Einlagerungsprotokoll

## Quellenregel

HGB §§ 467-475h: gesetze-im-internet.de. UZK (VO 952/2013): eur-lex.europa.eu. ADSp 2017: dslv.org. Zollverwaltung.de für ATLAS. Unsicherheit bleibt sichtbar.

## 2. `ihl-028-transportversicherung`

**Fokus:** Internationales Handelsrecht: Transportversicherung im internationalen Handel. Institute Cargo Clauses A/B/C (Lloyd's), All-Risk vs. benannte Gefahren, Versicherungspflicht nach Incoterms CIF/CIP, Versicherungszertifikat für Akkreditive und Subrogation.

# Transportversicherung im internationalen Handel

## Worum es geht

Die Transportversicherung (Cargo Insurance) sichert Warenrisiken auf dem internationalen Transport. Die Institute Cargo Clauses (ICC A, B, C) der Lloyd's Market Association sind weltweiter Standard. CIF-Klausel verpflichtet Verkäufer zur Mindestversicherung (ICC C — benannte Gefahren); CIP (Incoterms 2020) verlangt umfassende ICC A-Deckung.

## Kernnormen / Kernquellen

- **Institute Cargo Clauses (A) 2009**: All-Risk-Deckung (mit benannten Ausschlüssen)
- **Institute Cargo Clauses (B) 2009**: Benannte Gefahren plus Erdbeben/Vulkan/Blitz
- **Institute Cargo Clauses (C) 2009**: Minimaldeckung — nur grobe Gefahren
- **Incoterms 2020 CIF A5**: Verkäufer: Mindestversicherung ICC (C) oder gleichwertig
- **Incoterms 2020 CIP A5**: Verkäufer: ICC (A) oder gleichwertig (Upgrade ab 2020)
- **UCP 600 Art. 28**: Versicherungsdokument — Mindestdeckung, Indossierung, Datum

## Schlüsselbegriffe

- ICC A ("All Risks"): Deckung aller Gefahren außer ausdrücklich Ausgeschlossenen (Krieg, Streik separat)
- ICC C: Grunddeckung — Feuer, Explosion, Schiffbruch, Kollision, Strandung, Abwurf
- Institute War Clauses, Institute Strikes Clauses: Zusatzdeckung für Kriegs- und Streikrisiken
- Open Cover Policy: Rahmendeckung für alle Sendungen des Versicherungsnehmers
- Subrogation: Versicherer tritt in Rechte des Versicherten gegen Frachtführer nach Schadensersatz

## Typische Streitfragen / Anwendungsfälle

1. Akkreditiv verlangt Versicherungszeugnis: Welche Mindestanforderungen nach UCP 600 Art. 28?
2. CIF mit ICC (C): Reicht das für Elektronikware? (Nein — Diebstahl nicht gedeckt in ICC C)
3. Kriegsklausel: Gilt Standarddeckung ICC A für Transportschäden durch Sabotage?
4. Subrogation: Frachtführer haftungsbeschränkt (CMR 8,33 SZR/kg) — zahlt Versicherer Rest?
5. Open Cover: Anzeigepflichten bei ungewöhnlichen Sendungen?

## Methodik

- Versicherungsbedarfsanalyse: Warenwert, Transportmodus, Länderrisiko
- CIF-Vertrag: Käufer ggf. Zusatzversicherung abschließen (CIF nur ICC C-Minimum)
- Versicherungszertifikat: Blank-Indossament für Akkreditivzwecke
- Kriegsrisikogebiete: Lloyd's Market Association Annual War Notice prüfen

## Output

- ICC A/B/C Vergleichstabelle (Gefahren, Ausschlüsse)
- Versicherungszertifikat-Checkliste (UCP 600 Art. 28)
- Open-Cover-Klausel-Muster

## Quellenregel

ICC A/B/C 2009: lloyds.com (LMA). UCP 600 Art. 28: iccwbo.org. Incoterms 2020: iccwbo.org. Schrifttum: Tetley, Marine Cargo Claims (4. Aufl. 2008). Unsicherheit bleibt sichtbar.

## 3. `ihl-029-warentransit-und-gefahruebergang`

**Fokus:** Internationales Handelsrecht: Gefahrübergang bei auf Reise befindlicher Ware nach CISG Art. 68 und Incoterms 2020. Verkauf auf Reise (string trading), Rückwirkungsfiktion, Dokumentengefahr und Absicherung durch Transportversicherung.

# Warentransit und Gefahrübergang

## Worum es geht

CISG Art. 68 regelt den Gefahrübergang beim Verkauf von Ware, die sich bereits auf dem Transportweg befindet (goods in transit, string trading). Die Gefahr geht grundsätzlich auf den Käufer über, wenn der Vertrag geschlossen wird — rückwirkend ab Übergabe an den Frachtführer, es sei denn, der Verkäufer kannte den Schaden und verschwieg ihn.

## Kernnormen / Kernquellen

- **CISG Art. 68**: Gefahrübergang bei auf Reise befindlicher Ware — Vertragsschluss als Zeitpunkt
- **CISG Art. 67**: Gefahrübergang bei Versendungskauf (regulärer Fall)
- **CISG Art. 69**: Gefahrübergang bei Abholung und ohne Beförderungsvertrag
- **Incoterms 2020 CIF/CFR**: Gefahrübergang nach Verladung — für String Trading geeignet
- **UCP 600 Art. 20**: On-Board-Datum als Gefahrübergangsbeleg

## Schlüsselbegriffe

- String trading: Wiederverkauf während Transport (Rohstoffe, Commodities)
- Rückwirkungsfiktion Art. 68: Gefahr ab Frachtführerübergabe (retroaktiv)
- Dokumentengefahr: wer Papiere hält, hält das Risiko (bei Konnossement)
- Verkäufer-Arglist: Art. 68 S. 2 — kannte Schaden und verschwieg ihn → keine Gefahrübergabe
- Versicherungszeugnis: transit buyer braucht Versicherungsbescheinigung

## Typische Streitfragen / Anwendungsfälle

1. Ölladung auf Tanker auf Reise verkauft — Schiff sinkt nach Vertragsabschluss: Wer trägt Verlust?
2. Art. 68 Satz 2: Wie beweist Käufer, dass Verkäufer Schaden kannte?
3. String Trading: Wie viele Weiterverkäufe sind rechtlich zulässig ohne neues Transportdokument?
4. Dokumentenerwerb (BL-Indossament): Geht Gefahr mit Konnossement-Übertragung über?
5. Transportversicherung im String: Wer versichert bei CIF-Weiterverkauf?

## Methodik

- Art. 68 CISG: Stichtag Gefahrübergang = Datum Vertragsschluss (nicht Lieferung)
- String Trading: Versicherungskette prüfen — jeder Käufer braucht Nachweis
- Dokumentenprüfung: On-Board-Datum im BL bestätigt Frachtführer-Übergabe
- Arglist-Ausnahme: immer als Gegenargument prüfen

## Output

- Gefahrübergangs-Zeitstrahl (CISG Art. 67/68/69 im Vergleich)
- String-Trading-Dokumentenfluss
- Versicherungszeugnis-Anforderungen für String Buyer

## Quellenregel

CISG Art. 67-69: uncitral.un.org. Schrifttum: Schlechtriem/Schwenzer Art. 68 (2019). Incoterms 2020: iccwbo.org. Unsicherheit bleibt sichtbar.

## 4. `ihl-030-zolltarif-und-ursprung`

**Fokus:** Internationales Handelsrecht: Zolltarif (EU Kombinierte Nomenklatur, HS-Code) und nicht-präferenzieller Ursprung nach UZK Art. 59-63. Einreihung von Waren, wesentliche Be- und Verarbeitung, ursprungsbestimmende Vorgänge und Antidumping-Relevanz.

# Zolltarif und nicht-präferenzieller Ursprung

## Worum es geht

Die zollrechtliche Einreihung (HS-Code / KN-Code) bestimmt den Zollsatz und Regelungsrahmen (Antidumping, Sanktionen, Exportkontrolle). Der nicht-präferenzielle Ursprung nach UZK Art. 59-63 bestimmt "Made in X" für Handelspolitikmaßnahmen. Der präferenzielle Ursprung (Freihandelsabkommen) gilt für Zollpräferenzen (separat — siehe ihl-031).

## Kernnormen / Kernquellen

- **UZK Art. 56-58**: Zolltarifmaßnahmen und Klassifizierung
- **UZK Art. 59-63**: Nicht-präferenzieller Ursprung — wesentliche Be- und Verarbeitung
- **Kombinierte Nomenklatur (KN) VO (EWG) 2658/87**: EU-Warennomenklatur (8-stellig)
- **HS-Übereinkommen 1983 (WZO)**: Harmonisiertes System — 6-stellige Basis
- **Durchführungsverordnung (EU) 2015/2447**: Erläuterungen zu UZK-Ursprungsregeln
- **WTO Ursprungsabkommen (AoRO) 1994**: WTO-Rahmen für nichtpräferenzielle Ursprungsregeln

## Schlüsselbegriffe

- HS-Code: 6-stellig global harmonisiert; KN: 8-stellig EU; TARIC: 10-stellig EU
- Ursprung nach letzter wesentlicher Be- und Verarbeitung: wirtschaftlich gerechtfertigte Verarbeitung
- Tarifsprung (Change of Tariff Heading): Wechsel der Zolltarifposition als Ursprungsregel
- Ad-valorem-Wertschöpfungsregel: Mindestanteil Wertschöpfung im Ursprungsland
- Ursprungszeugnis: IHK-Zeugnis als Nachweis für nicht-präferenziellen Ursprung

## Typische Streitfragen / Anwendungsfälle

1. Einreihungsstreit: Ware kann in KN-Position X oder Y fallen — wie entscheiden?
2. Ursprungsbestimmung China oder Vietnam: Verlagerung nur der letzten Verarbeitungsstufe?
3. Antidumping-Umgehung: Neue Ursprungsregeln für chinesische Waren nach Verarbeitung in Drittland?
4. Bindendes Zolltarifrecht (BTI): Wie beantragen, welche Bindungswirkung?
5. Ursprungszeugnis nach Brexit: Gilt EUR.1 noch zwischen EU und UK?

## Methodik

- Einreihung: Allgemeine Vorschriften KN (AV 1-6) anwenden; Zolltarif-Auskunft (TARIC-online) nutzen
- Ursprung: Produktionsprozess dokumentieren; wesentliche Be- und Verarbeitung nachweisen
- BTI beantragen: Bindende Zolltarifauskunft beim Hauptzollamt / EU-Datenbank EBTI
- Antidumping-Verdacht: EuG-Rspr. zu Umgehungsfällen (curia.europa.eu)

## Output

- HS-Code-Einreihungsschema (AV 1-6)
- Ursprungsnachweis-Anforderungen (UZK Art. 61)
- BTI-Antragsformular-Hinweise

## Quellenregel

UZK (VO 952/2013): eur-lex.europa.eu. TARIC: ec.europa.eu/taxation_customs. KN (VO 2658/87): eur-lex.europa.eu. WZO HS: wcoomd.org. Unsicherheit bleibt sichtbar.
