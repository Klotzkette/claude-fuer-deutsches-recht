---
name: cloud-act-und-drittstaat-pruefen
description: "Für Cloud Act und Drittstaat prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Cloud Act und Drittstaat prüfen

## Fachkern: Cloud Act und Drittstaat prüfen

- **KI-/Berufsrechtsproblem (Cloud Act und Drittstaat prüfen):** Prüfe Auslandsbezug des KI-Anbieters nach Absatz vier der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). EU/EWR sind regelmäßig leichter vertretbar; Drittstaaten benötigen eine eigene Berufsgeheimnisprüfung. US-CLOUD Act, FISA, Supportzugriffe, EU-US-DPF, SCC und Professional Secrecy Addendum sauber trennen.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

## Norm

Absatz 4 der jeweiligen Dienstleisterregelung. Wortlaut (am Beispiel § 43e Abs. 4 BRAO; identisch in § 62a Abs. 4 StBerG, § 50a Abs. 4 WPO, § 39c Abs. 4 PAO; bei § 26a BNotO entsprechend):

"Bei der Inanspruchnahme von Dienstleistungen, die im Ausland erbracht werden, darf der Rechtsanwalt dem Dienstleister den Zugang zu fremden Geheimnissen unbeschadet der übrigen Voraussetzungen dieser Vorschrift nur dann eröffnen, wenn der dort bestehende Schutz der Geheimnisse dem Schutz im Inland vergleichbar ist, es sei denn, dass der Schutz der Geheimnisse dies nicht gebietet."

## Berufsrechtliche Auslegungslinie

Der Sitz des Anbieters in der EU oder im EWR ersetzt die Prüfung der tatsächlichen Leistungs-, Support-, Backup- und Unterauftragnehmerstandorte nicht. Bei Auslandsleistungen ist die Vergleichbarkeit des Geheimnisschutzes nach [Paragraf 43e Absatz 4 BRAO](https://www.gesetze-im-internet.de/brao/__43e.html) zu prüfen, soweit dessen Ausnahme nicht greift; das gilt auch innerhalb der EU und des EWR. Weitere beteiligte Personen sind nach Absatz 3 einzubeziehen. Die datenschutzrechtlichen Anforderungen bleiben nach Absatz 8 daneben bestehen.

Wichtig: Die Vergleichbarkeit bezieht sich auf den Schutz der Geheimnisse, nicht auf das allgemeine Rechtsschutzniveau. Selbst wenn ein Land eine funktionierende Justiz hat, kann der Schutz von Berufsgeheimnissen mangelhaft sein.

## Problemzone USA

Die USA stellen die größte praktische Herausforderung dar, weil die meisten KI-Anbieter dort ansässig sind oder dort verarbeiten lassen.

### CLOUD Act (2018)

Der US-Clarifying Lawful Overseas Use of Data Act verpflichtet US-Anbieter und ihre weltweiten Töchter, US-Behörden auf Anordnung Zugang zu Daten zu gewähren, auch wenn diese außerhalb der USA gespeichert sind. Eine deutsche Hostinglokation schützt also nicht.

### FISA Section 702

FISA Section 702 kann unter bestimmten Voraussetzungen Zugriffe auf elektronische Kommunikation von Nicht-US-Personen über US-Dienste ermöglichen. Für die Kanzlei genügt deshalb nicht die Frage "Wo steht der Server?", sondern es sind Konzern-, Support-, Administrations- und Herausgabezugriffe mitzudenken.

### Konsequenz

Bei US-Anbietern kann ein struktureller Restzugriff durch US-Behörden bestehen, der mit dem deutschen Berufsgeheimnis kollidieren kann. Daraus folgt nicht automatisch ein Totalverbot; erforderlich sind aber eine sorgfältige Abwägung, Datenminimierung, Vertragszusätze und dokumentierte Restrisikoentscheidung.

## Professional Secrecy Addendum

Bei US-Anbietern empfehlenswert: ein eigenes Berufsgeheimnis-Addendum zum Hauptvertrag, das

- die berufsrechtlichen Anforderungen explizit übernimmt
- den Anbieter zur Anfechtung jedes US-Auskunftsverlangens verpflichtet
- den Anbieter zur unverzüglichen Information der Kanzlei verpflichtet, soweit gesetzlich zulässig
- den Anbieter zur Datenminimierung in Richtung USA verpflichtet (keine US-Backups, keine US-Logs)
- Gerichtsstand und anwendbares Recht in Deutschland

Ob ein Anbieter solche Zusätze akzeptiert, muss am konkreten Vertragsstand live geprüft werden. Keine Produktbehauptung aus Modellwissen übernehmen.

## Prüfschema

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Punkt | Status | Ampel | Bemerkung |
|---|---|---|---|
| Sitz Anbieter (Hauptvertragspartei) | | | |
| Konzernzugehörigkeit (US-Konzern?) | | | |
| Verarbeitungsstandort | | | |
| Backup-Standort | | | |
| Modellanbieter (etwa OpenAI) Standort | | | |
| Hoster Standort | | | |
| CLOUD-Act-Anwendbarkeit | | | |
| FISA-Anwendbarkeit | | | |
| Professional Secrecy Addendum | | | |
| Gerichtsstand Deutschland | | | |
| Anwendbares deutsches Recht | | | |
| Standardvertragsklauseln (SCC) | | | |
| Adequacy decision (EU-US-DPF) | | | |

## EU-US-Data Privacy Framework

Das 2023 in Kraft getretene Data Privacy Framework regelt den datenschutzrechtlichen Datentransfer in die USA. **Es regelt nicht das Berufsgeheimnis.** Es schützt nicht vor CLOUD-Act-Zugriffen. Der DPF ist datenschutzrechtlich relevant, berufsrechtlich nur als Indiz für ein gewisses Schutzniveau, nicht als Genehmigung.

## Empfehlungen

- Bei EU/EWR-Anbietern: tatsächliche Leistungs- und Zugriffsorte einschließlich Support und Unterauftragnehmer prüfen; keine Freigabe allein nach Sitz oder Hostingangabe.
- Bei US-Bezug: konkrete behördliche Zugriffsmöglichkeiten und wirksame vertragliche sowie technische Schutzmaßnahmen prüfen; ein Berufsgeheimnis-Addendum oder EU-Hosting belegt für sich noch keine Zulässigkeit.
- Bei sonstigen Drittstaaten: Schutz der Geheimnisse und Zugriffsmöglichkeiten am konkreten Leistungsort feststellen. Keine automatische Länderampel; ungeklärte Vergleichbarkeit ist eine offene Freigabevoraussetzung, keine durch Risikoakzeptanz ersetzbare Prüfung.

## Zentrale Normen (Paragrafenkette)

- Art. 44–49 DSGVO — Drittlandsübermittlung, SCC, Adequacy Decisions, CBPR
- Art. 46 Abs. 2 lit. c DSGVO — Standardvertragsklauseln als geeignete Garantien
- § 43e Abs. 4 BRAO, § 62a Abs. 4 StBerG, § 50a Abs. 4 WPO — Drittstaat-Klausel Berufsrecht
- US CLOUD Act 2018, 18 U.S.C. § 2713 — Zugriff auf Daten unabhängig vom Speicherort
- FISA Section 702, 50 U.S.C. § 1881a — Überwachung elektronischer Kommunikation von Nicht-US-Personen

## Triage-Frage (Entscheidungsbaum)

1. Welche Stellen erbringen die Leistung oder können auf Geheimnisse zugreifen, und in welchen Ländern?
2. Bei Auslandsleistungen den vergleichbaren Geheimnisschutz nach Paragraf 43e Absatz 4 BRAO einschließlich der gesetzlichen Ausnahme begründen. Sitz und Konzernzugehörigkeit liefern Anhaltspunkte, keine abschließende Freigabe.
3. Konkrete Zugriffsrechte, Vertragsbindungen und technische Schutzmaßnahmen prüfen; Datenschutz und Berufsgeheimnis getrennt bewerten.
4. Fehlende Nachweise gezielt nachfordern. Die betroffene Nutzung erst bei erfüllten gesetzlichen Voraussetzungen empfehlen; sonst erforderliche Beschränkung oder Alternative benennen.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu prüfen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — US-Anbieter in Kanzleiinfrastruktur prüfen | Cloud-Act-Risikobewertung nach Schema unten |
| Variante A — kein US-Bezug erkennbar | Drittstaat-Kapitel trotzdem prüfen (UK TIOPA, CN DSL) |
| Variante B — Mandant will trotz Risiko US-Anbieter nutzen | Risikohinweis dokumentieren; Mandant schriftlich bestaetigen lassen |
| Variante C — staatliche Ermittlung laeuft bereits | Sofortiger Wechsel; Datensicherung und Incident-Response prüfen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — Drittstaat-Prüfvermerk

**Adressat:** Kanzlei intern — Tonfall: sachlich-juristisch

```
Drittstaat-Prüfvermerk [DATUM]
Anbieter: [NAME, LAND]
Konzernstruktur: [US-Konzern ja/nein; Mutter: NAME]

A) DSGVO-Drittlandsübermittlung (Art. 44 DSGVO)
Adequacy Decision: [ja/nein; EU-US-DPF ja/nein]
SCC vorhanden: [ja/nein; Datum]
TIA (Transfer Impact Assessment) durchgefuehrt: [ja/nein]

B) Berufsrechtlicher Drittstaat-Check (§ 43e Abs. 4 BRAO)
Vergleichbarkeit Schutzniveau: [ja/eingeschraenkt/nein]
CLOUD-Act-Risiko: [ja/nein/unklar]
Professional Secrecy Addendum: [vorhanden/nicht vorhanden/beantragt]

C) Ampel
DSGVO-Transfer: GRUEN / GELB / ROT
Berufsrecht Drittstaat: GRUEN / GELB / ROT
Empfehlung: [Nutzung freigegeben / Addendum erforderlich / Anbieterwechsel]
```

--- vor Versand klären ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
