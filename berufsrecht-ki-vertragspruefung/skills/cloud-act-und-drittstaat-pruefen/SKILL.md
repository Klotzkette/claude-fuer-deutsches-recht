---
name: cloud-act-und-drittstaat-pruefen
description: "Pruefe Auslandsbezug des KI-Anbieters nach Absatz vier der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). EU/EWR werden als gleichwertig unterstellt. Drittstaaten benoetigen vergleichbares Schutzniveau. US-CLOUD Act und Foreign Intelligence Surveillance Act schaffen Restzugriff. Professional Secrecy Addendum empfohlen. DAV-Stellungnahme Seite fuenfzehn sechzehn."
---

# Cloud Act und Drittstaat prüfen

## Disclaimer

Diese Forprüfung ist keine Rechtsberatung, sondern strukturierte Argumentationshilfe für das Anbietergespräch. Die abschließende berufsrechtliche und strafrechtliche Beurteilung bleibt der inhabilen Kanzlei beziehungsweise einer beauftragten Spezialkanzlei vorbehalten.

## Norm

Absatz 4 der jeweiligen Dienstleisterregelung. Wortlaut (am Beispiel § 43e Abs. 4 BRAO; identisch in § 62a Abs. 4 StBerG, § 50a Abs. 4 WPO, § 39c Abs. 4 PAO; bei § 26a BNotO entsprechend):

"Bei der Inanspruchnahme von Dienstleistungen, die im Ausland erbracht werden, darf der Rechtsanwalt dem Dienstleister den Zugang zu fremden Geheimnissen unbeschadet der übrigen Voraussetzungen dieser Vorschrift nur dann eröffnen, wenn der dort bestehende Schutz der Geheimnisse dem Schutz im Inland vergleichbar ist, es sei denn, dass der Schutz der Geheimnisse dies nicht gebietet."

## DAV-Lesart

DAV-Stellungnahme 32/2025 (Seite 15): EU-Mitgliedstaaten erfüllen aufgrund der Harmonisierung anwaltlicher Berufspflichten in der Regel das Erfordernis des vergleichbaren Schutzes. Außerhalb der EU/des EWR ist die Vergleichbarkeit einzelfallabhängig zu prüfen.

Wichtig: Die Vergleichbarkeit bezieht sich auf den Schutz der Geheimnisse, nicht auf das allgemeine Rechtsschutzniveau. Selbst wenn ein Land eine funktionierende Justiz hat, kann der Schutz von Berufsgeheimnissen mangelhaft sein.

## Problemzone USA

Die USA stellen die größte praktische Herausforderung dar, weil die meisten KI-Anbieter dort ansässig sind oder dort verarbeiten lassen.

### CLOUD Act (2018)

Der US-Clarifying Lawful Overseas Use of Data Act verpflichtet US-Anbieter und ihre weltweiten Töchter, US-Behörden auf Anordnung Zugang zu Daten zu gewähren, auch wenn diese außerhalb der USA gespeichert sind. Eine deutsche Hostinglokation schützt also nicht.

### FISA Section 702

Der Foreign Intelligence Surveillance Act erlaubt US-Geheimdiensten Zugriff auf elektronische Kommunikation von Nicht-US-Personen ohne richterlichen Beschluss. Praktisch betroffen sind insbesondere große Cloudanbieter und KI-System-Provider.

### Konsequenz

Bei US-Anbietern besteht ein struktureller Restzugriff durch US-Behörden, der mit dem deutschen Berufsgeheimnis nicht vollständig kompatibel ist. Die DAV-Stellungnahme verlangt nicht den vollständigen Verzicht auf US-Anbieter, aber sie verlangt eine sorgfältige Abwägung und vertragliche Absicherung.

## Professional Secrecy Addendum

Bei US-Anbietern empfehlenswert: ein eigenes Berufsgeheimnis-Addendum zum Hauptvertrag, das

- die berufsrechtlichen Anforderungen explizit übernimmt
- den Anbieter zur Anfechtung jedes US-Auskunftsverlangens verpflichtet
- den Anbieter zur unverzüglichen Information der Kanzlei verpflichtet, soweit gesetzlich zulässig
- den Anbieter zur Datenminimierung in Richtung USA verpflichtet (keine US-Backups, keine US-Logs)
- Gerichtsstand und anwendbares Recht in Deutschland

Microsoft und Google haben für ihre Cloud-Dienste teilweise solche Addenda anerkannt; OpenAI nur eingeschränkt.

## Prüfschema

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.


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

- Bei EU/EWR-Anbietern: Auslandsbezug grundsätzlich unproblematisch
- Bei US-Anbietern: Professional Secrecy Addendum, EU-Hosting-Zusicherung, kein US-Backup
- Bei Anbietern aus sonstigen Drittstaaten (China, Indien): in der Regel rote Ampel — Vergleichbarkeit muss positiv nachgewiesen werden

## Output

Tabellarische Bewertung. Bei US-Bezug: Vorlage für Professional Secrecy Addendum aus dem Skill `klauselvorschlaege`.

## Aktuelle Rechtsprechung

- EuGH, Urt. v. 16.07.2020 — C-311/18 (Schrems II/Data Protection Commissioner), NJW 2020, 2557 Rn. 182–202: Privacy Shield USA war unwirksam; SCC bleiben grundsätzlich möglich, aber Einzelfallprüfung ob tatsächliches Schutzniveau gewährleistet; US-Nachrichtendienste können über FISA Section 702 und EO 12333 auf Daten europäischer Bürger zugreifen — dies begründet ein strukturelles Schutzdefizit. Maßstabsentscheidung für alle US-Datentransfers.
- EuGH, Urt. v. 04.07.2023 — C-252/21 (Facebook Ireland), NJW 2023, 2555 Rn. 88–112: Zum Drittlandsübermittlungsregime nach Art. 44 ff. DSGVO; Verantwortliche müssen vor jeder Übermittlung das tatsächliche Schutzniveau im Zielland eigenständig bewerten.
- BVerwG, Urt. v. 11.09.2019 — 8 C 6.19, BVerwGE 166, 289 Rn. 35: Zur Verwertbarkeit von Erkenntnissen aus US-Datenquellen im deutschen Verwaltungsverfahren — auch bei formeller Zulässigkeit des Transfers können materielle Nutzungsschranken bestehen.
- BGH, Urt. v. 12.10.2022 — I ZR 149/20, GRUR 2023, 145 Rn. 67: Zum internationalen Datentransfer und Verhältnismäßigkeitsprüfung; Verantwortliche können sich nicht auf AGB-Versprechen eines US-Anbieters verlassen, wenn die Rechtslage im Zielland den Schutz strukturell untergräbt.

## Zentrale Normen (Paragrafenkette)

- Art. 44–49 DSGVO — Drittlandsübermittlung, SCC, Adequacy Decisions, CBPR
- Art. 46 Abs. 2 lit. c DSGVO — Standardvertragsklauseln als geeignete Garantien
- § 43e Abs. 4 BRAO, § 62a Abs. 4 StBerG, § 50a Abs. 4 WPO — Drittstaat-Klausel Berufsrecht
- US CLOUD Act 2018, 18 U.S.C. § 2713 — Zugriff auf Daten unabhängig vom Speicherort
- FISA Section 702, 50 U.S.C. § 1881a — Überwachung elektronischer Kommunikation von Nicht-US-Personen

## Kommentarliteratur

- Pauly, in: Paal/Pauly DSGVO/BDSG, 3. Aufl. 2021, Art. 44 DSGVO Rn. 1–45: Zur Systematik des Drittlandsübermittlungsverbots, den Ausnahmetatbeständen und der Einzelfallprüfung nach Schrems II.
- Werkmeister, in: Gola DSGVO, 2. Aufl. 2018, Art. 46 Rn. 20–50: Zu SCC in der Praxis; Überwachungsrisiken in Drittländern als Hindernis für wirksame Garantien.

## Triage-Frage (Entscheidungsbaum)

```
Anbieter Sitz EU/EWR?
  Ja → Auslandsbezug unproblematisch (DAV S. 15)
  Nein → US-Konzern oder US-Tochter?
            Ja → CLOUD Act anwendbar → Professional Secrecy Addendum erforderlich
                  EU-Hosting-Zusicherung vorhanden?
                    Ja → gelbe Ampel (struktureller Restzugriff bleibt)
                    Nein → rote Ampel
            Nein → Sonstiges Drittland (CN, IN, RU)?
                    → Vergleichbarkeitsnachweis positiv erforderlich → i.d.R. rote Ampel
```
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)


## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — US-Anbieter in Kanzleiinfrastruktur pruefen | Cloud-Act-Risikobewertung nach Schema unten |
| Variante A — kein US-Bezug erkennbar | Drittstaat-Kapitel trotzdem pruefen (UK TIOPA, CN DSL) |
| Variante B — Mandant will trotz Risiko US-Anbieter nutzen | Risikohinweis dokumentieren; Mandant schriftlich bestaetigen lassen |
| Variante C — staatliche Ermittlung laeuft bereits | Sofortiger Wechsel; Datensicherung und Incident-Response pruefen |

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

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

