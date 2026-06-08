---
name: facto
description: "Facto im Plugin Fachanwalt Vergaberecht: prüft konkret De-facto-Vergabe ohne Ausschreibung angreifen, Bieter-Eignungsprüfung im Vergabeverfahren prüfen, Vergabe freiberuflicher Leistungen (Architekten, Ingenieure. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Facto

## Arbeitsbereich

**Facto** ordnet den Fall über die tragenden Prüfungslinien: De-facto-Vergabe ohne Ausschreibung angreifen, Bieter-Eignungsprüfung im Vergabeverfahren prüfen, Vergabe freiberuflicher Leistungen (Architekten. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `fachanwalt-vergaberecht-de-facto-vergabe-klage` | De-facto-Vergabe ohne Ausschreibung angreifen: Bieter stellt fest dass öffentlicher Auftraggeber Auftrag direkt vergeben hat. Normen: § 135 GWB (Unwirksamkeit), §§ 160 ff. GWB (Nachprüfungsantrag VK), § 132 GWB (wesentliche Vertragsaenderung). Prüfraster: Aufdeckung der direkten Vergabe, Schadensersatzanspruch § 181 GWB, Unwirksamkeitsklage, Ausnahme-Tatbestaende. Output Klageschrift-Geruest, Schadensbeschreibung. Abgrenzung: Regulaerer Nachprüfungsantrag siehe fachanwalt-vergaberecht-nachprüfungsantrag-vk; Unterschwelle siehe mandat-triage-vergaberecht. |
| `fachanwalt-vergaberecht-eignungspruefung` | Bieter-Eignungsprüfung im Vergabeverfahren prüfen: Bieter wurde ausgeschlossen oder will Eignung nachweisen. Normen: § 122 GWB (Eignungskriterien), §§ 123 und 124 GWB (Ausschlussgründe), § 125 GWB (Selbstreinigung), § 50 VgV (EEE). Prüfraster: Befähigung, Zuverlässigkeit, wirtschaftliche/finanzielle/technische Leistungsfähigkeit, Eigenerklarung EEE, Selbstreinigung. Output Eignungsnachweis-Paket oder Angriff gegen Ausschluss. Abgrenzung: Gesamtnachprüfungsantrag siehe fachanwalt-vergaberecht-nachprüfungsantrag-vk; IT-Sicherheits-Eignung siehe fachanwalt-vergaberecht-it-sicherheits-vergabe-bsi-it-sig-2. |
| `fachanwalt-vergaberecht-freiberufliche-leistungen-hoai` | Vergabe freiberuflicher Leistungen (Architekten, Ingenieure, Rechtsanwaelte, Wirtschaftspruefer): Auftraggeber will HOAI- und vergaberechtskonform vergeben. Normen: § 50 VgV (Freiberufliche Leistungen), §§ 73 ff. VgV (Planungswettbewerb), HOAI 2021 (nach EuGH C-377/17 BGH VII ZR 174/19 als Orientierung), RPW 2013. Pruefraster: Verfahrenswahl Verhandlungsverfahren mit/ohne TW, Honorar als Wertungskriterium, Mindest- und Hoechstsaetze nach EuGH-Entscheidung, Planungswettbewerb RPW. Output Verfahrensentwurf, Honorar-Wertungsmodul. Abgrenzung: Wertung siehe fachanwalt-vergaberecht-zuschlagskriterien-wertungsschema. |
| `fachanwalt-vergaberecht-inhouse-interkommunal` | Inhouse-Geschaeft und interkommunale Zusammenarbeit vergaberechtlich pruefen: öffentlicher Auftraggeber will ohne Ausschreibung an verbundene Einrichtung oder Schwester-Kommune vergeben. Normen: § 108 GWB (Ausnahmen), Teckal-Doktrin EuGH C-107/98, Hamburg-Stadtreinigung EuGH C-480/06. Pruefraster: Kontrolltest wie ueber eigene Dienststelle, Wesentlichkeitstest 80 Prozent Taetigkeit für Kontrollierende, Privatkapitalverbot mit Ausnahmen, horizontale Zusammenarbeit § 108 Abs. 6 GWB. Output Inhouse-Pruefvermerk, Vertragsentwurf-Modul. Abgrenzung: De-facto-Vergabe siehe fachanwalt-vergaberecht-de-facto-vergabe-klage. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `fachanwalt-vergaberecht-de-facto-vergabe-klage`

**Fokus:** De-facto-Vergabe ohne Ausschreibung angreifen: Bieter stellt fest dass öffentlicher Auftraggeber Auftrag direkt vergeben hat. Normen: § 135 GWB (Unwirksamkeit), §§ 160 ff. GWB (Nachprüfungsantrag VK), § 132 GWB (wesentliche Vertragsaenderung). Prüfraster: Aufdeckung der direkten Vergabe, Schadensersatzanspruch § 181 GWB, Unwirksamkeitsklage, Ausnahme-Tatbestaende. Output Klageschrift-Geruest, Schadensbeschreibung. Abgrenzung: Regulaerer Nachprüfungsantrag siehe fachanwalt-vergaberecht-nachprüfungsantrag-vk; Unterschwelle siehe mandat-triage-vergaberecht.

# De-facto-Vergabe-Klage

## Zweck

Klage gegen ohne Ausschreibung erfolgte Auftragsvergabe.

## 1) De-facto-Vergabe — Begriff

- Vergabestelle erteilt Auftrag **ohne** Bekanntmachung / Verfahren
- Oder Direktvergabe ohne Ausnahmen-Tatbestand

### Beispiele

- Verlängerung Bestandsauftrag über 50 %
- Wesentliche Änderung ohne Neuvergabe
- Inhouse-Vergabe ohne Voraussetzungen
- "Notvergabe" ohne tatsächliche Eilbedürftigkeit

## 2) Unwirksamkeits-Klage § 135 GWB

### Voraussetzungen

- De-facto-Vergabe oder Pflichtverstoß
- Antrag bei VK / Klage

### Folgen

- Vertrag wird unwirksam
- Rückabwicklung
- Neuvergabe erforderlich

### Frist

- 30 Tage nach Kenntnis
- 6 Monate nach Vertragsschluss

## 3) Inhouse-Vergabe Voraussetzungen

### EuGH-Linie (Teckal-Kriterien)

- Kontrolle wie über eigene Dienststelle
- Wesentliche Tätigkeit für Eigentuemer
- Keine Beteiligung privater Kapitals

### Prüfung § 108 GWB

- Detaillierte Voraussetzungen
- Bei Verstoß: De-facto-Vergabe

## 4) Schadensersatz § 181 GWB

### Voraussetzungen

- Pflichtverletzung Vergabestelle
- Eigene Bewerbung
- Schaden

### Höhe

- Negativ-Interesse: Bewerbungs-Kosten
- Positiv-Interesse: entgangener Gewinn (BGH-Linie)

## 5) Aufdeckung

### Phase 1 — Information

- Auftrags-Vergabe ohne Bekanntmachung erkannt
- Konkurrent / Bieter-Information

### Phase 2 — Beweis-Sammlung

- Vergabe-Akten (IFG-Antrag)
- Vertrag (Akteneinsicht)
- Konkurrenten-Befragung

### Phase 3 — Klage VK / OLG

- Unwirksamkeits-Antrag
- Schadensersatz-Anspruch

## 6) IFG-Antrag § 5 IFG

### Prüfung

- Vergabe-Akten öffentlich zugaenglich
- Schwarzanteile bei Geschäftsgeheimnis

### Frist

- 1 Monat Antrags-Behandlung
- Bei Schweigen: Klage

## 7) Typische Konstellationen

### Versorgungs-Verträge

- Strom, Gas, Telekom
- Vertrags-Verlängerung ohne Ausschreibung

### IT-Verträge

- Modular-Erweiterungen
- Lock-In-Faktor missbraucht

### Bauauftraege

- Folge-Aufträge ohne Neuvergabe
- Nachtraege über Schwelle

## 8) Typische Fehler

1. **30-Tage-Frist verpasst**
2. **IFG-Antrag nicht gestellt**
3. **Schadensersatz-Anspruch pauschal**
4. **Inhouse-Vergabe-Voraussetzungen falsch geprüft**

## 9) BGH-/EuGH-Linien (Stand 05/2026, verifiziert curia.europa.eu / openjur.de)

- **EuGH 11.06.2009, C-300/07 (Hans & Christophorus Oymanns)**: Begriff des öffentlichen Auftraggebers nach RL 2004/18; Krankenkassen als Einrichtungen öffentlichen Rechts. Quelle: curia.europa.eu (CELEX 62007CJ0300).
- **EuGH 19.12.2018, C-216/17 (Coopservice)**: Ausschreibungspflicht Rahmenvereinbarungen; Volumenbegrenzungen zwingend. Quelle: curia.europa.eu.
- **EuGH 28.10.2020, C-521/18 (Pegaso)**: Vergabe ohne wettbewerbliches Verfahren — De-facto-Vergabe ist nichtig nach Art. 2d RL 89/665 / § 135 GWB, wenn EU-weite Bekanntmachung pflichtwidrig unterblieben ist. Quelle: curia.europa.eu.
- **EuGH 27.11.2019, C-402/18 (Tedeschi)**: Direktvergabe — Inhouse-Voraussetzungen § 108 GWB / Art. 12 RL 2014/24 strikt: Kontrolle wie eigene Stelle, > 80% Taetigkeit für kontrollierende Behörde, keine private Kapitalbeteiligung. Quelle: curia.europa.eu.

Aktuelle OLG-Vergabesenat-Entscheidungen vor Ausgabe per olg-... bzw. openjur.de mit Aktenzeichen und Datum verifizieren.

## Anschluss

- `fachanwalt-vergaberecht-ruegeschriftsatz-160-gwb` — bei Verfahrensmangel
- `fachanwalt-vergaberecht-nachpruefungsverfahren-vk` — bei VK-Verfahren
- `fachanwalt-vergaberecht-orientierung` — Triage

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — De-facto-Vergabe Klage § 135 GWB | Feststellungsantrag VK; Template unten |
| Variante A — Auftrag bereits vollstaendig abgewickelt | § 135 Abs. 2 GWB Antrag moegliche weise verfristet; Schadensersatz § 181 GWB |
| Variante B — Inhouse-Ausnahme streitig | § 108 GWB Voraussetzungen pruefen; eigentuemlicher Sachverhalt |
| Variante C — Unterhalb EU-Schwellenwert | Primaerechtsschutz; Haushaltsrecht statt GWB |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Vertiefung: Output-Template de-facto-Vergabe

### Triage — Bevor losgelegt wird, klaere:

1. Wurde Auftrag ohne jedes Vergabeverfahren erteilt?
2. Liegt der Auftragswert ueber EU-Schwellenwert?
3. Bestand Auftraggeberpflicht zur Ausschreibung (kein Inhouse, kein In-state)?
4. Wurde § 135 GWB Feststellungsantrag rechtzeitig gestellt (30 Tage nach Bekanntmachung, max. 6 Monate)?
5. Alternativ: § 181 GWB Schadensersatz?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

### Output-Template Antrag Feststellung Unwirksamkeit § 135 GWB
**Adressat:** Vergabekammer — Tonfall: sachlich-juristisch

```
Vergabekammer [NAME]

Antrag auf Feststellung der Unwirksamkeit des Zuschlags
nach § 135 Abs. 1 GWB

Antragsteller: [BIETER]
Antragsgegner: [AUFTRAGGEBER]

Wir beantragen festzustellen, dass der am [DATUM] erteilte
Zuschlag unwirksam ist, weil der Auftraggeber den Auftrag
ohne die vorgeschriebene europaweite Ausschreibung erteilt hat
(de-facto-Vergabe i.S.d. § 135 Abs. 1 Nr. 2 GWB).

Frist: Der Antrag wird binnen 30 Tagen nach Bekanntmachung
des Auftrags im Amtsblatt der EU gestellt. Hilfsweise binnen
6 Monaten nach Vertragsschluss (§ 135 Abs. 2 GWB).

[Rechtsanwalt/-anwaeltin]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 2. `fachanwalt-vergaberecht-eignungspruefung`

**Fokus:** Bieter-Eignungsprüfung im Vergabeverfahren prüfen: Bieter wurde ausgeschlossen oder will Eignung nachweisen. Normen: § 122 GWB (Eignungskriterien), §§ 123 und 124 GWB (Ausschlussgründe), § 125 GWB (Selbstreinigung), § 50 VgV (EEE). Prüfraster: Befähigung, Zuverlässigkeit, wirtschaftliche/finanzielle/technische Leistungsfähigkeit, Eigenerklarung EEE, Selbstreinigung. Output Eignungsnachweis-Paket oder Angriff gegen Ausschluss. Abgrenzung: Gesamtnachprüfungsantrag siehe fachanwalt-vergaberecht-nachprüfungsantrag-vk; IT-Sicherheits-Eignung siehe fachanwalt-vergaberecht-it-sicherheits-vergabe-bsi-it-sig-2.

# Eignungsprüfung

## Kaltstart-Rückfragen

1. Welche Eignungskriterien hat der Auftraggeber in der Bekanntmachung aufgestellt — Befähigung, wirtschaftliche/finanzielle Leistungsfähigkeit, technische/berufliche Leistungsfähigkeit?
2. Welche Eigenerklärungen oder Nachweise wurden gefordert (PQ-Verzeichnis DTVP, EEE § 50 VgV, Einzelnachweise wie Referenzen, Umsatzzahlen, Haftpflichtversicherung)?
3. Liegen beim Mandanten oder bei einem Konkurrenten Ausschlussgründe vor — § 123 GWB (zwingend) oder § 124 GWB (fakultativ)?
4. Wurden Selbstreinigungsmaßnahmen § 125 GWB ergriffen und dokumentiert (Schadensersatz, Aufklärung, Compliance-Maßnahmen)?
5. Beanstandet der Mandant die eigene Ablehnung, oder soll die Eignung eines Konkurrenten angegriffen werden?
6. Wird die Eignungsleihe § 47 VgV in Anspruch genommen — liegt Verfügungserklärung des Dritten vor?
7. Sind die Eignungskriterien verhältnismäßig zum Auftrag (§ 122 Abs. 4 GWB), oder diskriminierend?
8. Wird die Auswahlentscheidung bei eingeschränkter Teilnehmerzahl (nichtoffenes Verfahren) beanstandet?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Kernauszug)

- **§ 122 Abs. 1 GWB** — Geeignet sind nur Unternehmen, die die Kriterien zu Befähigung und Erlaubnis zur Berufsausübung, wirtschaftlicher und finanzieller sowie technischer und beruflicher Leistungsfähigkeit erfüllen.
- **§ 122 Abs. 2 GWB** — Eignungskriterien dürfen nur gefordert werden soweit durch den Auftragsgegenstand gerechtfertigt. Buchst. a: Befähigung und Erlaubnis; b: wirtschaftliche und finanzielle Leistungsfähigkeit; c: technische und berufliche Leistungsfähigkeit.
- **§ 122 Abs. 4 GWB** — Eignungskriterien müssen mit dem Auftragsgegenstand in Verbindung stehen, verhältnismäßig sein und dürfen nicht diskriminierend wirken.
- **§ 123 GWB** — Zwingende Ausschlussgründe: rechtskräftige Verurteilung wegen Bildung krimineller Vereinigungen (§ 129 StGB), Bestechung (§§ 334, 335 StGB), Betrug (§§ 263, 264 StGB), Geldwäsche (§ 261 StGB), Terrorismusfinanzierung (§ 89c StGB), Menschenhandel (§ 232 StGB); außerdem erhebliche Steuer- und Sozialversicherungsrückstände sowie bestimmte Ordnungswidrigkeiten.
- **§ 124 GWB** — Fakultative Ausschlussgründe: erhebliche oder fortdauernde Mängel bei Ausführung eines früheren Auftrags, die Schaden verursacht haben (Nr. 7); schwere Verfehlung im beruflichen Bereich (Nr. 3); Verfolgung wettbewerbsbeschränkender Absprachen (Nr. 4); Interessenkonflikte nicht behebbar (Nr. 5); Verzerrung des Wettbewerbs durch Vorarbeit (Nr. 6); Insolvenz, Zahlungsunfähigkeit (Nr. 2).
- **§ 125 GWB** — Selbstreinigung: Bieter ist trotz Ausschlussgrund geeignet, wenn er a) der geschädigten Stelle Schadensersatz geleistet hat, b) aktiv mit Ermittlungsbehörden kooperiert und die Sachlage umfassend aufgeklärt hat und c) konkrete technische, organisatorische und personelle Maßnahmen ergriffen hat.
- **§ 47 VgV** — Eignungsleihe: Bieter kann Eignungskriterien unter bestimmten Voraussetzungen durch Kapazitäten anderer Unternehmen erfüllen; Verfügungserklärung erforderlich; bei baulichen oder spezifischen Leistungen Haftungsübernahme des Dritten.
- **§ 50 VgV** — Eigenerklärung (EEE); Einheitliche Europäische Eigenerklärung als vorläufiger Eignungsnachweis; Einzelnachweise nur vom voraussichtlichen Zuschlagsempfänger.
- **§§ 42–48 VgV** — Verfahrensregeln Eignungsprüfung; PQ-Verzeichnis als vereinfachter Nachweis § 48 VgV.

### Leitentscheidungen (Stand 05/2026, verifizierbare Quellen)

| Gericht | Aktenzeichen | Datum | Kernaussage | Quelle |
|---|---|---|---|---|
| EuGH | C-376/21 (Zamestnik) | 03.06.2022 | Ausschluss wegen Falschangaben — Verhaeltnismaessigkeitspruefung im Einzelfall obligatorisch (Art. 57 RL 2014/24) | curia.europa.eu |
| EuGH | C-66/22 (Infraestruturas) | 21.12.2023 | Ausschluss wegen Wettbewerbsverstoss § 124 Abs. 1 Nr. 4 GWB / Art. 57 Abs. 4 RL — Auslegung „schwerwiegende Verfehlung im beruflichen Bereich" | curia.europa.eu |
| EuGH | C-66/20 | 12.05.2022 | Selbstreinigung Art. 57 Abs. 6 RL — Bewertung obliegt national; Verhaeltnismaessigkeit der Ausschlussfolgen | curia.europa.eu |
| VK Bund / OLG Vergabesenate | laufende Senatsrspr. 2023-2025 | — | PQ-Verzeichnis ersetzt Einzelnachweise; Zusatznachweise nur ausnahmsweise zulaessig | bundeskartellamt.de/Vergabe + olg-duesseldorf.nrw.de |

Konkrete OLG-Vergabesenat-Entscheidungen vor Verwendung per olg-duesseldorf.nrw.de / openjur.de mit Aktenzeichen und Datum verifizieren.

## Prüfschema in Tabellenform

| Nr. | Prüfschritt | Norm | Ergebnis |
|---|---|---|---|
| 1 | Eignungskriterien aus Bekanntmachung extrahieren | § 122 GWB | Kategorien: Befähigung, wirtschaftlich, technisch |
| 2 | Verhältnismäßigkeit jedes Kriteriums prüfen | § 122 Abs. 4 GWB | Unverhältnismäßig → Rüge bis Angebotsabgabe |
| 3 | EEE vollständig ausgefüllt? | § 50 VgV | Fehlen → Ausschluss wegen formaler Mängel |
| 4 | PQ-Verzeichnis eingetragen und aktuell? | § 48 VgV | Veralteter PQ-Eintrag → Aktualisierung erforderlich |
| 5 | Zwingende Ausschlussgründe § 123 GWB? | § 123 GWB | Vorliegend → Ausschluss zwingend; Selbstreinigung § 125 GWB |
| 6 | Fakultative Ausschlussgründe § 124 GWB? | § 124 GWB | Vorliegen → Ermessensentscheidung AG |
| 7 | Selbstreinigung § 125 GWB vollständig dokumentiert? | § 125 GWB | Alle drei Elemente: Schadensersatz, Aufklärung, Compliance |
| 8 | Eignungsleihe § 47 VgV — Verfügungserklärung vorhanden? | § 47 VgV | Fehlt → kein wirksamer Rückgriff auf Dritteignung |
| 9 | Mindestanforderungen angemessen (Umsatz, Referenzen)? | § 45 Abs. 3, § 46 VgV | Jahresumsatz nicht mehr als 2-facher Auftragswert; OLG Düsseldorf Verg 21/18 |
| 10 | Eigenerklärung ausreichend oder Nachweise erforderlich? | § 50 Abs. 2 VgV | Einzelnachweise nur vom Zuschlagsempfänger |
| 11 | Eignungsprüfung Konkurrent — Akteneinsicht beantragt? | § 165 GWB | Ohne Einsicht kaum substanziiert rügbar |
| 12 | Auswahlentscheidung (nichtoffenes Verfahren) nachvollziehbar? | § 51 VgV | Auswahlkriterien bekannt? Punktevergabe dokumentiert? |
| 13 | Bietergemeinschaft — Eignungsanforderungen erfüllt? | § 44 VgV | Gesamteignung ausreichend; kein Mitglied hat Ausschlussgrund |
| 14 | Nachforderungsrecht AG ausgeübt? | § 56 Abs. 2 VgV | AG darf fehlende Unterlagen nachfordern; nicht bei inhaltlichen Mängeln |
| 15 | Rüge vorbereitet? | § 160 Abs. 3 GWB | Frist: bis Angebotsabgabe bei erkennbarem Fehler in Bekanntmachung |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Eignungspruefung VK-Verfahren | Ruegeschriftsatz / NPA; Template unten |
| Variante A — Eignungsanforderung unverhaaltnismaessig | Ruege § 160 Abs. 3 GWB; alternativ Nachpruefungsantrag |
| Variante B — Bieter bereits ausgeschlossen | Sofortige Ruege; Stillhaltefrist laeuft |
| Variante C — Selbstreinigung nach Ausschlussgrund | § 125 GWB Selbstreinigung nachweisen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 — Stellungnahme Selbstreinigung § 125 GWB

```
An [Auftraggeber / Vergabestelle] [Datum]
Betr.: Vergabeverfahren [Titel], Az. [...]
 Stellungnahme Selbstreinigung § 125 GWB

Sehr geehrte Damen und Herren,

namens und in Vollmacht der [Bieter-GmbH] nehmen wir zu dem
mitgeteilten Ausschlussgrund § 124 Abs. 1 Nr. [...] GWB
(schwere Verfehlung im beruflichen Bereich) Stellung.

I. Sachverhalt (§ 125 Abs. 1 Nr. 2 GWB — Aufklärung)

Am [Datum] erging wegen [Sachverhalt] gegen [Mitarbeiter/GmbH]
[Urteil / Bußgeld / Einstellung gegen Auflage], Az. [...].
Schaden in Höhe von EUR [Betrag] ist entstanden.

Unsere Mandantin hat den Vorgang von sich aus vollständig
aufgeklärt, aktiv mit [Staatsanwaltschaft / Kartellamt] kooperiert
(Anlage K1: Kooperationsschreiben) und interne Untersuchung durch
externe Rechtsanwälte durchführen lassen (Abschlussbericht
Anlage K2).

II. Schadensersatz (§ 125 Abs. 1 Nr. 1 GWB)

Mit [Geschädigtem] wurde am [Datum] ein Vergleich über
EUR [Betrag] geschlossen (Anlage K3). Damit ist der Schaden
vollständig ausgeglichen.

III. Compliance-Maßnahmen (§ 125 Abs. 1 Nr. 3 GWB)

a) Einführung eines ISO 37301-zertifizierten Compliance-Management-
 Systems am [Datum] (Anlage K4: Zertifikat).
b) Schulung aller Vertriebs- und Beschaffungsmitarbeiter am
 [Datum] und jährlich seitdem (Anlage K5: Teilnehmerlisten).
c) Entlassung der involvierten Personen [Name, Position] mit
 Datum [Datum] (Anlage K6).
d) Einrichtung eines anonymen Hinweisgebersystems (Whistleblower-
 Hotline) seit [Datum] (Anlage K7).

IV. Verhältnismäßigkeit (§ 125 Abs. 2 GWB)

Die Maßnahmen sind unter Berücksichtigung der Schwere und der
besonderen Umstände des Einzelfalls geeignet und ausreichend,
um eine Wiederholung zu verhindern. Der Vorgang liegt [X] Jahre
zurück. Seitdem ist die Mandantin ohne Beanstandung tätig.

Wir beantragen festzustellen, dass der Ausschlussgrund nicht
mehr einschlägig ist und das Angebot in die Wertung einzubeziehen
ist.

[Rechtsanwälte]
```

### Baustein 2 — Rüge wegen überzogener Eignungsanforderungen

```
An [Vergabestelle] [Datum]
Betr.: Vergabe [Titel], Rüge § 160 Abs. 3 GWB
 Unverhältnismäßige Eignungsanforderungen

Sehr geehrte Damen und Herren,

wir rügen unverzüglich nach Kenntnisnahme folgenden Vergabeverstoß:

Pkt. [X] der Bekanntmachung vom [Datum] fordert als Mindest-
eignungskriterium einen Jahresumsatz von EUR [Betrag] im
Bereich [Leistungsgebiet]. Dieser Betrag entspricht dem
[X-fachen] des geschätzten Auftragswerts.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
§ 122 Abs. 4 GWB ist ein Mindestjahresumsatz von mehr als dem
Zweifachen des Auftragswerts unverhältnismäßig. Das geforderte
Kriterium liegt erheblich darüber und schließt wirtschaftlich
gesunde mittelständische Unternehmen diskriminierend aus.

Wir fordern Sie auf, die Anforderung auf das Zweifache des
geschätzten Auftragswerts (EUR [Betrag]) zu reduzieren und
die Vergabeunterlagen entsprechend anzupassen.

[Rechtsanwälte]
```

### Baustein 3 — Rüge Eignungsbejahung Konkurrent

```
An [Vergabestelle] [Datum]
Betr.: Vergabe [Titel], Rüge § 160 Abs. 3 GWB
 Unberechtigte Eignungsbejahung Beigeladener

Sehr geehrte Damen und Herren,

unsere Mandantin beanstandet, dass die [Beigeladene GmbH] zu
Unrecht als geeignet behandelt wurde.

1. Fehlendes Eignungskriterium: Die Bekanntmachung vom [Datum]
 verlangt [konkrete Anforderung, z.B. ISO 27001-Zertifikat].
 Die Beigeladene verfügt nach unserem Kenntnisstand über kein
 solches Zertifikat (Anlage K1: öffentlich zugängliche Liste).

2. Obligatorischer Ausschlussgrund § 123 Abs. 4 Nr. 2 GWB:
 Die Beigeladene hat in dem am [Datum] veröffentlichten
 Vergabeverfahren [Az.] Kartellanteile getragen, was durch
 Pressemitteilung des Bundeskartellamts vom [Datum] belegt ist
 (Anlage K2). Ein zwingender Ausschlussgrund liegt vor.

Wir fordern Sie auf, die Beigeladene vom Verfahren auszuschließen.

[Rechtsanwälte]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Beweislast und Darlegungslast

| Frage | Beweislast |
|---|---|
| Eigene Eignung | Bieter (EEE, Einzelnachweise auf Anforderung) |
| Verhältnismäßigkeit Eignungskriterien | Auftraggeber im Nachprüfungsverfahren |
| Ausschlussgrund § 123 GWB | Auftraggeber (Nachweis der Verurteilung) |
| Fakultativer Ausschlussgrund § 124 GWB | Auftraggeber (Ermessensausübung dokumentieren) |
| Selbstreinigung § 125 GWB — ausreichend | Bieter (vollständige Dokumentation der 3 Elemente) |
| Eignungsleihe — tatsächliche Verfügbarkeit | Bieter (Verfügungserklärung + Haftungsübernahme) |
| Eignungsmangel Konkurrent | Antragsteller muss substantiierte Anhaltspunkte darlegen |

## Fristen und Verjährung

| Frist | Dauer | Anker | Norm |
|---|---|---|---|
| Rüge Eignungsfehler in Bekanntmachung | bis Angebotsabgabe | Ablauf Angebotsfrist | § 160 Abs. 3 Nr. 2, 3 GWB |
| Rüge nach Eignungsablehnung | 10 Kalendertage | Kenntnis Ablehnung | § 160 Abs. 3 Nr. 1 GWB |
| Nachprüfungsantrag nach Rügen-Ablehnung | 15 Kalendertage | Ablehnungsschreiben | § 160 Abs. 3 Nr. 4 GWB |
| Wirkungsdauer obligatorischer Ausschluss § 123 | bis zu 5 Jahre | Rechtskräftige Verurteilung | § 123 Abs. 3 GWB |
| Wirkungsdauer fakultativer Ausschluss § 124 | bis zu 3 Jahre | Ereignis | § 124 Abs. 2 GWB |
| Schadensersatz § 181 GWB | 3 Jahre | § 199 Abs. 1 BGB | §§ 195, 199 BGB |

## Typische Gegenargumente und Reaktion

| Einwand | Reaktion |
|---|---|
| Eignungsanforderungen verhältnismäßig — Markteindruck | Konkret darlegen: Auftragswert vs. geforderter Umsatz; Marktdaten zu Zertifizierungsstand |
| Selbstreinigung unvollständig — Schadensersatz nicht nachgewiesen | Vergleichsvertrag mit Zahlungsbeleg; keine Vollständigkeitspflicht wenn Schaden noch offen |
| Eignungsleihe unzulässig bei bauspezifischen Leistungen | § 47 Abs. 1 Satz 2 VgV lässt Einschränkungen zu; prüfen ob Auftraggeber Einschränkung in Bekanntmachung aufgenommen hat |
| Selbstreinigung-Bewertung pauschal abgelehnt | EuGH C-66/20 (12.05.2022): Bewertung der Selbstreinigung muss verhaeltnismaessig und einzelfallbezogen erfolgen |
| Konkurrent hat parallele Ausschlussmaßnahme laufen | Offenes Strafverfahren genügt nicht für § 123 GWB; rechtskräftige Verurteilung erforderlich |
| AG verweigert Akteneinsicht | EuGH C-376/21 (03.06.2022) + § 165 GWB: Akteneinsicht in geschwaerzter Form; Geheimhaltungsschutz und Rechtsschutz abwaegen |

## Streitwert und Kosten

- Eignungsstreitigkeiten: Streitwert = Auftragswert (netto); RVG-Gebühren entsprechend.
- VK-Verfahren: Gebühren § 182 GWB (2500–50000 EUR); typisch 4000–8000 EUR bei mittelgroßen Aufträgen.
- Schadensersatz § 181 GWB: Vertrauensschaden (nachgewiesene Angebotskosten); Erfüllungsinteresse selten.

## Strategische Empfehlung

- **Eigene Ablehnung wegen Eignungsmangel:** Rüge unverzüglich; ggf. gleichzeitig Nachbesserungsangebot an AG; VK-Antrag bei Nichtabhilfe; Akteneinsicht § 165 GWB für Einzelheiten.
- **Selbstreinigung:** Vollständigkeit aller drei Elemente vor Angebotsabgabe sicherstellen; AG-Entscheidung ist Ermessenssache; VK prüft nur auf Ermessensfehler.
- **Eignungsmangel Konkurrent:** Ohne Akteneinsicht kaum substanziierbar; VK-Antrag mit Akteneinsichtsantrag kombinieren; nach Einsicht Ergänzung der Begründung.

## Anschluss-Skills

- `fachanwalt-vergaberecht-nachpruefungsantrag-vk` — vollständige Antragsstruktur
- `vergabe-nachpruefung-aussicht` — Prüfung Erfolgsaussichten
- `fachanwalt-vergaberecht-it-sicherheits-vergabe-bsi-it-sig-2` — IT-Sicherheits-Eignungskriterien

## Quellen (Stand 05/2026)

- GWB §§ 122–127, 123 (zwingende Ausschluesse), 124 (fakultative), 125 (Selbstreinigung), 160 (Nachpruefung), 165 (Akteneinsicht)
- VgV §§ 42–48, 50, 56 (Verfahrensregeln Eignung); §§ 47 (Eignungsleihe), 48 (PQ-Verzeichnis)
- VO (EU) 2014/24, insbes. Art. 57 (Ausschlussgruende); umgesetzt in §§ 123, 124 GWB
- EuGH C-376/21 (03.06.2022 — Falschangaben), C-66/22 (21.12.2023 — Wettbewerbsverstoss), C-66/20 (12.05.2022 — Selbstreinigung) — Volltext curia.europa.eu
- OLG-Vergabesenate (öffentliche Datenbanken der Landesjustiz)
- VK Bund: bundeskartellamt.de/Vergabe

## Vertiefung: Triage und Output-Template Eignungspruefung

### Triage — Bevor losgelegt wird, klaere:

1. Welches Eignungskriterium ist streitig? (Umsatz, Referenzen, Personal, Zertifikate, Insolvenz)
2. Ist Kriterium in Bekanntmachung oder Vergabeunterlagen eindeutig beschrieben? (§ 122 Abs. 4 GWB)
3. Wurde Eignungsanforderung im Verhaeltnis zum Auftragsgegenstand aufgestellt? (Verhaeltnismaessigkeit)
4. Liegt behaupteter Ausschluss § 124 GWB vor? (Harte/weiche Ausschlusskriterien)
5. Selbstreinigung nach § 125 GWB moeglich?

### Ergaenzende Leitsaetze Eignungspruefung (verifiziert curia.europa.eu)

- EuGH 03.06.2022, C-376/21 (Zamestnik) — Verhaeltnismaessigkeit bei Ausschluss wegen Falschangaben
- EuGH 21.12.2023, C-66/22 (Infraestruturas) — Auslegung der „schwerwiegenden Verfehlung im beruflichen Bereich"
- EuGH 12.05.2022, C-66/20 — Selbstreinigung Art. 57 Abs. 6 RL 2014/24
- EuGH 27.10.2016, C-292/15 — Transparenz auch unterhalb der Schwellenwerte bei grenzueberschreitendem Interesse

Vor Ausgabe konkrete Aktenzeichen ueber curia.europa.eu (EuGH) oder olg-... bzw. openjur.de verifizieren.

### Output-Template Begruendung Eignung
**Adressat:** Vergabestelle oder Vergabekammer — Tonfall: sachlich-juristisch

```
Stellungnahme zur Eignungspruefung
Vergabeverfahren [BEZEICHNUNG]

1. Eignungssachverhalt:
 Unser Mandant hat alle in der Bekanntmachung vom
 [DATUM] geforderten Eignungsnachweise fristgerecht
 eingereicht (Anlage K1 bis K[N]).

2. Zum streitigen Kriterium [XYZ]:
 [Konkreter Nachweis + BGH/EuGH-Bezug]
 Das Kriterium ist im Verhältnis zum Auftragsgegenstand
 verhaeltnismaessig nach § 122 Abs. 4 GWB / EuGH 03.06.2022,
 C-376/21 (curia.europa.eu).

3. Antrag:
 Unser Mandant ist als geeignet anzusehen.
 Ein Ausschluss wegen mangelnder Eignung ist
 rechtswidrig und aufzuheben.
```

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 3. `fachanwalt-vergaberecht-freiberufliche-leistungen-hoai`

**Fokus:** Vergabe freiberuflicher Leistungen (Architekten, Ingenieure, Rechtsanwaelte, Wirtschaftspruefer): Auftraggeber will HOAI- und vergaberechtskonform vergeben. Normen: § 50 VgV (Freiberufliche Leistungen), §§ 73 ff. VgV (Planungswettbewerb), HOAI 2021 (nach EuGH C-377/17 BGH VII ZR 174/19 als Orientierung), RPW 2013. Pruefraster: Verfahrenswahl Verhandlungsverfahren mit/ohne TW, Honorar als Wertungskriterium, Mindest- und Hoechstsaetze nach EuGH-Entscheidung, Planungswettbewerb RPW. Output Verfahrensentwurf, Honorar-Wertungsmodul. Abgrenzung: Wertung siehe fachanwalt-vergaberecht-zuschlagskriterien-wertungsschema.

# Freiberufliche Leistungen (§ 50 VgV)

## Aufgabe
Vergabe von Architekten-, Ingenieur-, Rechts-, Wirtschaftspruefer- und sonstigen freiberuflichen Leistungen vergaberechts- und honorarrechtskonform aufsetzen oder pruefen. Schluesselfrage: Welches Verfahren, wie Honorar in der Wertung beruecksichtigen?

## Einstieg
1. Leistung freiberuflich i. S. § 18 EStG?
2. Schwellenwert oberschwellig (Liefer-/Dienstleistung EUR 216000 Kommunen / EUR 140000 Bund ab 01.01.2026)?
3. Planungsleistung mit HOAI-Bezug (Architekt, Ingenieur)?
4. Planungswettbewerb sinnvoll (Architektur, Stadtplanung)?
5. Vergabesperre, fruehere Mandanten/Auftraggeber-Beziehungen, Interessenkonflikte (§§ 6 ff. VgV)?

## Verfahrenswahl
### Verhandlungsverfahren mit TW (Regel) § 50 VgV
Freiberufliche Leistungen sind regelmaessig nicht eindeutig und erschoepfend beschreibbar, daher Verhandlungsverfahren mit TW zulaessig. Voraussetzung § 14 Abs. 4 Nr. 5 VgV.

### Planungswettbewerb § 78 ff. VgV
Anonymisiertes Wettbewerbsverfahren mit Jury (RPW 2013). Anschluss-Vergabe an Sieger ueber Verhandlungsverfahren ohne TW (§ 14 Abs. 4 Nr. 8 VgV) zulaessig.

### Konzeptvergabe
Loesungsorientierte Vergabe ohne klassisches Leistungsverzeichnis; Eignung und Konzept werden gemeinsam bewertet.

## HOAI 2021 und EuGH/BGH-Linie
- EuGH C-377/17 Kommission/Deutschland (04.07.2019): Mindest- und Hoechstsaetze HOAI alte Fassung unionsrechtswidrig.
- BGH VII ZR 174/19 (02.06.2022): HOAI-Saetze im Bestand-Inland-Verhaeltnis nicht zwingend.
- HOAI 2021: Orientierungshilfe, kein zwingender Mindestpreis; freie Honorarvereinbarung moeglich.
- Vergabepraxis: Honorar als Wertungskriterium zulaessig und ueblich.

## Honorar als Wertungskriterium
- Grundsatz: zulaessig, aber nicht alleiniges Kriterium (qualitaetsabhaengige Leistung).
- Typische Gewichtung: 20-40 Prozent Honorar, 60-80 Prozent Qualitaet (Konzept, Team, Referenzen).
- Untergrenze: kein Preisdumping (§ 60 VgV Pruefung ungewoehnlich niedriger Angebote).

## Planungswettbewerb RPW 2013
- Anonymitaet bis Juryentscheidung.
- Preisgericht mit Mehrheit Fachleute.
- Preisgeld nach RPW-Tabellen.
- Direkter Anschluss an Sieger im Verhandlungsverfahren ohne TW (§ 14 Abs. 4 Nr. 8 VgV) zulaessig, sofern in Auslobung angekuendigt.

## Typische Fehler
- Honorar als einziges Kriterium (Qualitaetsverlust + EuGH-konformes Wertungsmodell verletzt).
- HOAI-Mindestsatz als Mindestpreis ausgeschrieben (unzulaessig nach EuGH).
- Planungswettbewerb ohne anonyme Phase.
- Bieterkreis im Verhandlungsverfahren zu eng (Mindestens 3 Bewerber).

## Output
- Verfahrensentwurf freiberufliche Leistung.
- Honorar-Wertungsmodul (Formel, Gewichtung, Pruefung niedriger Honorare).
- RPW-Wettbewerbs-Auslobungs-Geruest.

## Quellenregel
EuGH C-377/17 und BGH VII ZR 174/19 ueber curia.europa.eu und bundesgerichtshof.de verifizieren; HOAI 2021 i. d. F. der aktuellen Verordnung pruefen.

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.

## 4. `fachanwalt-vergaberecht-inhouse-interkommunal`

**Fokus:** Inhouse-Geschaeft und interkommunale Zusammenarbeit vergaberechtlich pruefen: öffentlicher Auftraggeber will ohne Ausschreibung an verbundene Einrichtung oder Schwester-Kommune vergeben. Normen: § 108 GWB (Ausnahmen), Teckal-Doktrin EuGH C-107/98, Hamburg-Stadtreinigung EuGH C-480/06. Pruefraster: Kontrolltest wie ueber eigene Dienststelle, Wesentlichkeitstest 80 Prozent Taetigkeit für Kontrollierende, Privatkapitalverbot mit Ausnahmen, horizontale Zusammenarbeit § 108 Abs. 6 GWB. Output Inhouse-Pruefvermerk, Vertragsentwurf-Modul. Abgrenzung: De-facto-Vergabe siehe fachanwalt-vergaberecht-de-facto-vergabe-klage.

# Inhouse und interkommunale Zusammenarbeit

## Aufgabe
Inhouse-Geschaeft oder horizontale interkommunale Zusammenarbeit als Ausnahme von der Ausschreibungspflicht pruefen. Fehlt eine Ausnahme, droht De-facto-Vergabe und § 135 GWB-Unwirksamkeit.

## Einstieg
1. Wer ist Auftraggeber, wer ist Auftragnehmer (gleicher öffentlicher Auftraggeber, Tochter, Schwester-Kommune)?
2. Beherrschungsstruktur (Anteile, Beirats-/Aufsichtsmehrheit)?
3. Privater Kapitalanteil am Auftragnehmer?
4. Wesentlichkeit: Mindestens 80 Prozent Taetigkeit für kontrollierende öffentliche Hand?
5. Bei horizontaler Kooperation: gemeinsames Ziel im Gemeinwohlinteresse?

## Pruefraster Inhouse § 108 Abs. 1-5 GWB
### 1. Kontrolltest
Auftraggeber muss aehnliche Kontrolle wie ueber eigene Dienststelle ausueben (Teckal-Doktrin EuGH C-107/98).
- Personelle Steuerung: Bestellung der Mehrheit der Leitungsorgane.
- Strategische Steuerung: Weisungsbefugnis.
- Auch durch gemeinsame Kontrolle mehrerer öffentlicher Auftraggeber moeglich (§ 108 Abs. 4 GWB).

### 2. Wesentlichkeitstest
Mindestens 80 Prozent der Taetigkeit des kontrollierten Auftragnehmers für die kontrollierende öffentliche Hand. Restliche Taetigkeiten nur nebenbei (EuGH C-340/04 Carbotermo).

### 3. Privatkapital
Grundsaetzlich keine private Beteiligung. Ausnahme § 108 Abs. 1 Nr. 3 GWB: bestimmte nicht-kontrollierende Beteiligungen aufgrund gesetzlicher Anordnung.

## Pruefraster Horizontale Kooperation § 108 Abs. 6 GWB
1. Auftraggeber kooperieren auf vertraglicher Basis.
2. Kooperation dient gemeinsamem Gemeinwohlziel.
3. Kooperation wird von rein öffentlichen Erwaegungen geleitet.
4. Weniger als 20 Prozent der vertragsgegenstaendlichen Taetigkeiten werden am Markt erbracht (EuGH C-480/06 Hamburg-Stadtreinigung).

## Vertragliche Umsetzung
- Inhouse-Vertrag: Gesellschafterstruktur, Kontrollrechte, Taetigkeitsbegrenzung, Reporting.
- Interkommunaler Vertrag: gemeinsames Ziel definieren, Marktteil < 20 Prozent festschreiben, Beendigungsrechte.

## Risiken bei Verlust der Inhouse-Eigenschaft
- Aufnahme privaten Kapitals -> Verlust Kontroll-Test.
- Steigender Marktanteil -> Verlust Wesentlichkeitstest.
- Fehlende Dokumentation -> Beweislast in Nachpruefungsverfahren beim Auftraggeber.
- Folge: De-facto-Vergabe, § 135 Abs. 1 Nr. 2 GWB -> Vertrag unwirksam.

## Output
- Inhouse-Pruefvermerk mit Kontrolltest, Wesentlichkeitstest, Privatkapital-Pruefung.
- Vertragsmodul Inhouse oder horizontale Kooperation.
- Monitoring-Konzept (Marktanteil, Kontrollstruktur).

## Quellenregel
EuGH-Linie (Teckal, Carbotermo, Hamburg-Stadtreinigung, Datenlotsen) und neuere BGH/OLG-Entscheidungen vor Ausgabe ueber curia.europa.eu und dejure.org verifizieren.

## Vergabe-Workbench-Boost v61.2

- Starte jedes Mandat mit Rolle, Verfahrensstand, Schwellenwert/Rechtsweg, Frist und Dokumentenlage.
- Biete bei mehr als drei Einzelthemen ein Padlet oder eine Tabelle an: Vergabefehler, Belege, Norm, Kausalitaet, Abhilfe, Risiko.
- Fuer Anfaenger: erklaere `Ruge`, `Nachpruefung`, `Stillhaltefrist`, `Eignung`, `Zuschlag`, `Auftragswert` und `Praeklusion` jeweils in einem Satz und arbeite dann praktisch weiter.
- Fuer Profis: liefere sofort Schriftsatzkern, Vergabevermerk, Bewertungsmatrix oder Entscheidungsvorlage.
- Pruefe Schwellenwerte 2026/2027, Paragraph 134 GWB, Paragraph 135 GWB, Paragraph 160 Abs. 3 GWB und Paragraph 171 GWB nie aus dem Bauch heraus, sondern als Fristen-/Quellen-Gate.
- Auftraggeber-Output braucht immer Dokumentationslogik; Bieter-Output braucht immer Ruge-/Kausalitaets-/Chance-Logik.
- Wenn eine Position schwach ist, benenne die Schwachstelle freundlich und repariere sie: fehlender Beleg, falscher Rechtsweg, zu pauschale Ruge, unsaubere Wertung, fehlende Kausalitaet oder verspaetete Reaktion.
