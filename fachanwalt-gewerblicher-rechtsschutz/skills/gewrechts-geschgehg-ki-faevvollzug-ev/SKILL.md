---
name: gewrechts-geschgehg-ki-faevvollzug-ev
description: "Gewrechts Geschgehg KI Faevvollzug EV im Plugin Fachanwalt Gewerblicher Rechtsschutz: prüft konkret Kollisionen zwischen gewerblichem Rechtsschutz NDA-Recht, KI-generierte Inhalte auf gewerblichen Rechtsschutz prüfen, EV-Vollziehungscheck. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Gewrechts Geschgehg KI Faevvollzug EV

## Arbeitsbereich

**Gewrechts Geschgehg KI Faevvollzug EV** ordnet den Fall über die tragenden Prüfungslinien: Kollisionen zwischen gewerblichem Rechtsschutz NDA-Recht, KI-generierte Inhalte auf gewerblichen Rechtsschutz prüfen, EV-Vollziehungscheck. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `fachanwalt-gewrechts-geschgehg-kollisionen-nda-hinschg-urhg` | Kollisionen zwischen gewerblichem Rechtsschutz NDA-Recht HinSchG und Urheberrecht prüfen wenn mehrere Schutzrechtsregime sich ueberschneiden. §§ 1 ff. GeschmMG § 14 MarkenG §§ 1 ff. HinSchG §§ 97 ff. UrhG. Prüfraster: Anwendungsbereich Vorrangfragen Schutzbereich Kollisionsauflösung Hinweisgeberschutz. Output: Kollisionsprüfmemo Handlungsempfehlung. Abgrenzung: Querschnitts-Skill für Kollisionsfragen. |
| `fachanwalt-gewrechts-ki-vo-50-genai` | KI-generierte Inhalte auf gewerblichen Rechtsschutz prüfen wenn GenAI-Outputs Schutzrechte beruehren. Art. 50 KI-VO Transparenzpflichten §§ 2 7 UrhG KI-Autorschaft. Prüfraster: Urheberrechtsschutz KI-Autorschaft Kennzeichnungspflicht Art. 50 KI-VO Verletzungsrisiken. Output: Compliance-Memo Empfehlungen für KI-Nutzung. Abgrenzung: nicht für allgemeine KI-Governance. |
| `faevvollzug-neu-001-ev-vollziehungscheck-dringlichkeit-titel-zus` | EV-Vollziehungscheck: Dringlichkeit, Titel und Zustellung bei einstweiliger Verfügung im gewerblichen Rechtsschutz. § 929 ZPO Vollziehungsfrist, § 936 ZPO, § 12 UWG, Selbstzustellung, Parteibetrieb, Rechtsfolgen verspäteter Vollziehung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `fachanwalt-gewrechts-geschgehg-kollisionen-nda-hinschg-urhg`

**Fokus:** Kollisionen zwischen gewerblichem Rechtsschutz NDA-Recht HinSchG und Urheberrecht prüfen wenn mehrere Schutzrechtsregime sich ueberschneiden. §§ 1 ff. GeschmMG § 14 MarkenG §§ 1 ff. HinSchG §§ 97 ff. UrhG. Prüfraster: Anwendungsbereich Vorrangfragen Schutzbereich Kollisionsauflösung Hinweisgeberschutz. Output: Kollisionsprüfmemo Handlungsempfehlung. Abgrenzung: Querschnitts-Skill für Kollisionsfragen.

## Mandantenfragen beim Kaltstart

1. Um welche Art von Information geht es (Quellcode, Kundenliste, Rezeptur, technisches Verfahren, Algorithmus, Finanzdaten)?
2. Welche konkreten Geheimhaltungsmaßnahmen hat das Unternehmen bisher getroffen (NDA, Zugriffskontrolle, Verschlüsselung, Schulungen)?
3. Wer hat die Information erlangt oder offenbart — ehemaliger Mitarbeiter, Lieferant, Wettbewerber, Journalist?
4. Besteht der Verdacht, dass die Information über einen Whistleblowing-Kanal (intern, BfJ, Öffentlichkeit) weitergegeben wurde?
5. Liegt ein NDA vor — wann geschlossen, welche Klauseln zur Geheimhaltungsdauer und Vertragsstrafe?
6. Welches Ziel verfolgt die Mandantschaft — einstweilige Verfügung, Schadensersatz, Strafanzeige oder Verteidigung gegen Vorwürfe?
7. Ist die Information möglicherweise auch urheberrechtlich oder patentrechtlich geschützt (Softwarecode, technische Erfindung)?
8. Handelt es sich um einen Sachverhalt mit Auslandsbezug (Wirtschaftsspionage, ausländischer Wettbewerber, grenzüberschreitende M&A)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| § 2 Nr. 1 GeschGehG | Legaldefinition Geschäftsgeheimnis: nicht allgemein bekannt, wirtschaftlicher Wert, angemessene Geheimhaltungsmaßnahmen, berechtigtes Interesse |
| § 3 GeschGehG | Erlaubte Handlungen: eigenständige Entwicklung, Reverse Engineering, Whistleblowing, Arbeitnehmer-Mitbestimmung |
| § 4 GeschGehG | Verbotene Handlungen: unbefugte Erlangung, Nutzung, Offenlegung |
| § 5 Nr. 2 GeschGehG | Whistleblower-Privileg: Geheimnisverletzung gerechtfertigt zur Aufdeckung rechtswidriger Handlungen im allgemeinen öffentlichen Interesse |
| §§ 6–8 GeschGehG | Zivilrechtliche Ansprüche: Unterlassung, Beseitigung, Vernichtung, Auskunft, Schadensersatz (drei Methoden) |
| §§ 9–14 GeschGehG | Prozessuale Sondervorschriften: Geheimhaltungsanordnung, beschränkter Personenkreis, Geheimnisklage |
| § 16 GeschGehG | Geheimhaltungsanordnung durch Gericht; Personenkreisbeschränkung |
| § 23 GeschGehG | Strafbarkeit Geheimnisverrat: bis 3 Jahre Freiheitsstrafe; bei Wirtschaftsspionage bis 5 Jahre |
| § 6 HinSchG | Verhältnis HinSchG zu anderen Vorschriften: GeschGehG-Schweigegebot tritt zurück |
| §§ 32, 36 HinSchG | Offenlegung als Ultima Ratio; Repressalienverbot mit Beweislastumkehr |
| § 40 HinSchG | Bußgeld bei Repressalie gegen Hinweisgeber bis EUR 50.000 |
| § 203 StGB | Verletzung von Privatgeheimnissen; Berufsgeheimnisträger inkl. Rechtsanwälte |
| §§ 43a BRAO, 2 BORA | Anwaltliche Verschwiegenheitspflicht |
| § 69a UrhG | Urheberrechtsschutz Software (Quellcode); Parallelschutz zu GeschGehG möglich |
| §§ 87a ff. UrhG | Datenbankschutz sui generis (15 Jahre, verlängerbar) |
| § 69e UrhG | Decompilation nur zur Herstellung von Interoperabilität erlaubt |
| Art. 6, 9, 35 DSGVO | Datenschutz bei Personalakten, Compliance-Untersuchungen, Datenschutz-Folgenabschätzung |
| § 26 BDSG | Beschäftigtendatenschutz bei internen Untersuchungen |

## Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---------|-------------|-------|-------------|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Vier-Stufen-Test § 2 Nr. 1 GeschGehG

| Stufe | Prüfpunkt | Praxis-Indikator | Rechtsfolge bei Fehlen |
|-------|-----------|-----------------|----------------------|
| 1 | Nicht allgemein bekannt / nicht ohne weiteres zugänglich | Branchenkenntnis, Fachliteratur, öffentliches Internet recherchiert? | Kein Geheimnisschutz |
| 2 | Wirtschaftlicher Wert wegen Geheimnischarakter | Negativwissen einbeziehen; Lizenzwert schätzen | Selten fehlend; Negativwissen reicht |
| 3 | Angemessene Geheimhaltungsmaßnahmen | Drei-Ebenen-Modell (organisatorisch, vertraglich, technisch) vollständig? | Häufigster Scheiterpunkt in der Rechtsprechung |
| 4 | Berechtigtes Geheimhaltungsinteresse | Illegal? Sittenwidrig? | Nur bei ausnahmsweise rechtswidrigem Inhalt fehlend |

## Prüfschema Geheimhaltungsmaßnahmen (Drei-Ebenen-Modell)

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Ebene | Mindestanforderungen | Dokumentationspflicht |
|-------|--------------------|-----------------------|
| Organisatorisch | Need-to-Know-Prinzip; Besucherregelung; Offboarding-Protokoll (Rückgabe Geräte, Sperrung Zugänge am letzten Arbeitstag); Schulungsnachweis | GHS-Policy schriftlich; Schulungsregister |
| Vertraglich | NDA mit Lieferanten, Beratern, Bewerbern, Praktikanten vor Datenzugang; Geheimhaltungsklausel Arbeitsvertrag; nachvertragliches Wettbewerbsverbot § 74 HGB mit Karenzentschädigung | NDA-Archiv; Unterschriften vollständig |
| Technisch | RBAC-Zugriffsrechte; Multi-Faktor-Authentifizierung; AES-256-Verschlüsselung at-rest/in-transit; DLP-Systeme; Endpoint-Logging; Klassifizierungsschema (öffentlich/intern/vertraulich/streng vertraulich) | Audit-Logs; Patch-Protokolle; SIEM-Exports |

## Prüfschema Ansprüche bei Verletzung

| Schritt | Prüfpunkt | Norm | Rechtsfolge |
|---------|-----------|------|-------------|
| 1 | Geschäftsgeheimnis-Status positiv (§ 2 Nr. 1)? | § 2 Nr. 1 GeschGehG | Anspruchsvoraussetzung |
| 2 | Verbotene Handlung (Erlangung, Nutzung, Offenlegung)? | § 4 GeschGehG | Anspruchsgrundlage |
| 3 | Rechtfertigungsgrund? | § 3, § 5 GeschGehG | Whistleblower-Privileg; Reverse Engineering; Meinungsfreiheit |
| 4 | Unterlassung und Beseitigung | § 6 GeschGehG | Kein Verschuldenserfordernis |
| 5 | Vernichtung / Rückruf / Herausgabe | § 7 GeschGehG | Verhältnismäßigkeit prüfen |
| 6 | Auskunft und Rechnungslegung | § 8 GeschGehG | Vorbereitung Schadensersatz |
| 7 | Schadensersatz: Methode wählen | § 10 GeschGehG | Konkreter Schaden / Verletzergewinn / fiktive Lizenzgebühr |
| 8 | Strafanzeige | § 23 GeschGehG | Freiheitsstrafe bis 5 Jahre bei Wirtschaftsspionage |
| 9 | Einstweilige Verfügung | §§ 935, 940 ZPO | Dringlichkeit binnen 1 Monat ab Kenntnis |

## Kollisionsfeld: GeschGehG vs. Urheberrecht

| Aspekt | GeschGehG | UrhG |
|--------|-----------|------|
| Schutzgegenstand | Information mit wirtschaftlichem Wert | Persönliche geistige Schöpfung |
| Entstehung | Mit Geheimhaltungsmaßnahmen | Automatisch mit Schöpfung |
| Dauer | Solange geheim | 70 Jahre nach Tod des Urhebers |
| Bei Veröffentlichung | Schutzverlust GeschGehG | UrhG bleibt bestehen |
| Software (§ 69a UrhG) | GeschGehG + UrhG parallel vor Open-Source-Release | Quellcode = Sprachwerk; Schutz ab Schöpfung |
| Datenbankrecht | §§ 87a ff. UrhG parallel zu GeschGehG | 15 Jahre Investitionsschutz sui generis |

## Kollisionsfeld: GeschGehG vs. HinSchG

| Prüfschritt | Inhalt | Norm |
|------------|--------|------|
| 1 | Verstößt der Hinweis-Gegenstand gegen Strafrecht / OWi / EU-Recht? | § 2 HinSchG |
| 2 | Whistleblower-Privileg greift ein | § 5 Nr. 2 GeschGehG |
| 3 | Interne oder externe Meldestelle (gleichberechtigt) | § 7 HinSchG |
| 4 | Öffentliche Offenlegung nur als Ultima Ratio | § 32 HinSchG |
| 5 | Repressalienverbot; Beweislastumkehr | § 36 HinSchG |
| 6 | Schadensersatz bei vorsätzlich falscher Meldung | § 38 HinSchG |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — GeschGehG-Kollision mit NDA / HinSchG / UrhG pruefen | Vier-Stufen-Test und Kollisionsfelder unten |
| Variante A — nur NDA ohne GeschGehG-Schutzmassnamen | NDA-Schutz schwaecher; GeschGehG nicht automatisch anwendbar |
| Variante B — Whistleblower-Situation nach HinSchG | GeschGehG tritt zurueck; HinSchG-Schutz pruefen |
| Variante C — Softwarecode als Geschaeftsgeheimnis | Urheberrecht und GeschGehG parallel; Schutzsystem definieren |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatz-Bausteine

### Antrag auf Geheimhaltungsanordnung § 16 GeschGehG

```
An das Landgericht [Ort] – [zuständige Kammer] –

In dem Verfahren [Az.] beantragen wir namens der Klägerin:

1. Das Gericht ordnet gemäß § 16 GeschGehG an, dass folgende in der Klageschrift
 und ihren Anlagen enthaltene Informationen als geheimhaltungsbedürftig einzustufen
 sind: [Konkrete Bezeichnung der Geschäftsgeheimnisse, z. B. Kundenliste
 Anlage K 3; Rezeptur Anlage K 5].

2. Zugang zu den als geheimhaltungsbedürftig eingestuften Informationen ist auf
 folgenden Personenkreis zu beschränken:
 a) die Prozessbevollmächtigten der Parteien,
 b) je eine benannte Parteivertretung,
 c) bestellte Sachverständige mit schriftlicher Vertraulichkeitspflicht.

Begründung:
Die bezeichneten Informationen erfüllen die Voraussetzungen des § 2 Nr. 1 GeschGehG
[Ausführung der vier Stufen]. Eine Offenlegung gegenüber der Öffentlichkeit oder
einem unbeschränkten Personenkreis würde den wirtschaftlichen Wert der Informationen
unwiederbringlich vernichten.

[Ort, Datum]
Rechtsanwalt/Rechtsanwältin [Name]
```

### Einstweilige Verfügung wegen Geheimnisverrat

```
An das Landgericht [Ort]

ANTRAG AUF ERLASS EINER EINSTWEILIGEN VERFÜGUNG
gemäß §§ 935, 940 ZPO iVm § 6 GeschGehG

Verfügungsklägerin: [Unternehmensname]
Verfügungsbeklagter: [Ehemaliger Mitarbeiter / Wettbewerber]

Es wird beantragt:

1. Der Verfügungsbeklagten wird es bei Meidung eines Ordnungsgeldes bis zu
 EUR 250.000, ersatzweise Ordnungshaft, untersagt, die in Anlage AS 1
 bezeichneten Informationen zu nutzen oder offenzulegen.

2. Der Verfügungsbeklagten wird aufgegeben, alle Kopien und Vervielfältigungen
 der Informationen gemäß Anlage AS 1 unverzüglich herauszugeben.

Dringlichkeit:
Die Verfügungsklägerin erlangte am [Datum] durch [Umstand] Kenntnis vom
Informationsabfluss. Der Antrag wird binnen [Tage] gestellt; eine
Selbstwiderlegung liegt nicht vor.

Glaubhaftmachung:
Eidesstattliche Versicherung [Name] (Anlage EV 1); Endpoint-Log-Auszug
(Anlage EV 2); E-Mail-Verkehr (Anlage EV 3).

[Ort, Datum]
Rechtsanwalt/Rechtsanwältin [Name]
```

### NDA-Klausel (HinSchG-Vorbehalt und Reverse-Engineering-Freigabe)

```
§ [X] Vertraulichkeit

(1) Die Parteien verpflichten sich, Vertrauliche Informationen gemäß § 2 Nr. 1
GeschGehG streng vertraulich zu behandeln und Dritten nicht ohne vorherige
schriftliche Zustimmung der offenbarenden Partei zugänglich zu machen.

(2) Diese Vereinbarung berührt nicht die Rechte nach dem Hinweisgeberschutzgesetz
(HinSchG). Meldungen über Rechtsverstöße an interne, externe oder — in den
Grenzen des § 32 HinSchG — öffentliche Meldestellen stellen keine Verletzung
dieser Vereinbarung dar.

(3) Erlaubt bleiben die in § 3 GeschGehG bezeichneten Handlungen, insbesondere
die eigenständige Entwicklung und das Reverse Engineering nach § 3 Abs. 1 Nr. 2
GeschGehG, soweit gesetzlich zulässig.

(4) Bei Verletzung dieser Vereinbarung ist eine Vertragsstrafe von EUR [Betrag]
je Verstoß zu zahlen, unbeschadet weitergehender Schadensersatzansprüche.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Beweislast

| Beweisthema | Beweislast | Beweismittel |
|------------|-----------|--------------|
| Geheimnischarakter (§ 2 Nr. 1 GeschGehG) | Kläger | GHS-Policy, Klassifizierungsregister, Schulungsnachweise |
| Angemessene Geheimhaltungsmaßnahmen | Kläger | RBAC-Protokolle, NDA-Archiv, IT-Audit-Berichte |
| Verbotene Handlung (§ 4 GeschGehG) | Kläger | Endpoint-Logs, E-Mail-Metadaten, Zeugen, forensische Auswertung |
| Rechtfertigungsgrund (§ 3, § 5 GeschGehG) | Beklagter | Nachweis Reverse Engineering, Whistleblowing-Meldung, Meinungsfreiheit |
| Schaden / Verletzergewinn | Kläger (nach Auskunft) | Buchhaltungsunterlagen Beklagter, Sachverständigengutachten |
| Repressalie gegen Hinweisgeber | Arbeitgeber bei Klage nach § 36 HinSchG | Beweislastumkehr: Arbeitgeber muss rechtmäßige Kündigung belegen |

## Fristen

| Frist | Inhalt | Norm |
|-------|--------|------|
| 1 Monat (ca.) | Dringlichkeit bei einstweiliger Verfügung; Selbstwiderlegungsrisiko | §§ 935, 940 ZPO |
| 3 Jahre | Regelverjährung Schadensersatzanspruch ab Kenntnis | §§ 195, 199 BGB |
| 1 Woche | Interne Meldestelle muss Eingang bestätigen | § 17 HinSchG |
| 3 Monate | Rückmeldung interne Meldestelle über ergriffene Maßnahmen | § 17 Abs. 2 HinSchG |
| 5 Jahre | Aufbewahrungsfrist für Meldungen und Dokumentation durch Meldestelle | § 11 HinSchG |
| Laufend | Jahresprotokoll Geheimhaltungsmaßnahmen empfohlen | § 2 Nr. 1 lit. c GeschGehG |

## Gegenargumente und Reaktion

| Gegenargument | Herkunft | Reaktion |
|--------------|---------|----------|
| "Die Information ist allgemein bekannt / im Internet abrufbar" | Beklagter | Konkrete Quellenrecherche; Unterschied zwischen teilweise bekannter Struktur und spezifischer Detailkombination |
| "Keine angemessenen Geheimhaltungsmaßnahmen — Klage scheitert" | Beklagter | Drei-Ebenen-Nachweis (org/vertragl/techn); ex-post-Dokumentation schadet nicht, wenn Maßnahmen tatsächlich bestanden |
| "Ich bin Hinweisgeber — § 5 Nr. 2 GeschGehG / HinSchG schützt mich" | Beklagter | Prüfen: Deckt HinSchG § 2 den Sachverhalt ab? War Meldung nur zu eigenem Vorteil oder tatsächlich öffentliches Interesse? |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Reverse Engineering nach § 3 GeschGehG erlaubt" | Beklagter | Prüfen: Produkt rechtmäßig erlangt? Keine AGB-Beschränkung (§ 307 BGB)? Keine Urheberrechtsverletzung (§ 69e UrhG)? |
| "NDA-Klausel ist nach § 307 BGB unwirksam" | Beklagter | Individualvertrag vs. AGB unterscheiden; bei Kaufmann § 310 BGB; Inhaltskontrolle trotzdem durchführen |

## Streitwert und Kosten

**Streitwert Unterlassung:** Orientierung am wirtschaftlichen Interesse der Klägerin; bei Kundenlisten EUR 50.000–500.000 je nach Umsatzrelevanz; bei technischen Verfahren bis in den Millionenbereich.

**Einstweilige Verfügung:** Streitwert i. d. R. 1/3 bis 1/2 des Hauptsachestreitwerts.

**Sachliche Zuständigkeit:** Landgericht ohne Streitwertgrenze (§ 15 GeschGehG); ggf. Konzentrationsgericht nach Landesrecht.

**Schadensberechnung (§ 10 GeschGehG, drei Methoden):**
1. Konkreter Schaden: entgangener Gewinn + Rechtsverteidigungskosten.
2. Verletzergewinn: vollständiger Abschöpfung des Gewinns des Verletzers.
3. Fiktive Lizenzgebühr: branchenübliche Lizenzrate auf den relevanten Umsatz (typisch 3–10 %).

**Strafbarkeit § 23 GeschGehG:**
- Abs. 1 (Erlangung): Freiheitsstrafe bis 3 Jahre oder Geldstrafe.
- Abs. 4 (Wirtschaftsspionage / Auslandsbezug): Freiheitsstrafe bis 5 Jahre.

## Strategische Empfehlung

| Situation | Empfehlung | Begründung |
|-----------|------------|-----------|
| Mitarbeiterabwanderung mit Datenmitnahme | Sofortiger eV-Antrag auf Unterlassung + Herausgabe; Strafanzeige § 23 GeschGehG parallel | Beweissicherung vor Datenlöschung; Abschreckungswirkung |
| Unternehmen will Schutz aufbauen | Drei-Ebenen-Maßnahmenkatalog; GHS-Policy; NDA-Update mit HinSchG-Vorbehalt | OLG Köln: fehlende IT-Kontrollen vernichten Schutz |
| Whistleblower verteidigen | § 5 Nr. 2 GeschGehG + § 36 HinSchG kombinieren; Beweislastumkehr nutzen | Arbeitgeber muss rechtmäßige Kündigung beweisen |
| M&A-NDA-Verhandlung | Pflichtklauseln: HinSchG-Vorbehalt, Reverse-Engineering-Freigabe, beidseitige Vertragsstrafe, Schiedsklausel DIS/ICC | Einseitige AG-NDA enthält regelmäßig HinSchG-Aushebelungen |
| Geheimnisklage LG | Sofort Geheimhaltungsanordnung § 16 GeschGehG beantragen; Personenkreis präzise benennen | Schutz vor weiterer Offenbarung im laufenden Verfahren |

## Anschluss-Skills

- `fachanwalt-arbeitsrecht-hinschg-whistleblower-repressalie` — HinSchG-Verteidigung im Arbeitsverhältnis
- `fachanwalt-gewerblicher-rechtsschutz-abmahnung-uwg` — UWG-Abmahnung bei unlauterem Geheimnisverrat
- `fachanwalt-gewerblicher-rechtsschutz-markenanmeldung` — Ergänzender Markenschutz für Produktnamen
- `fachanwalt-internationales-wirtschaftsrecht-cisg-pruefung` — Grenzüberschreitende NDA-Fragen

## Quellen

- GeschGehG: https://www.gesetze-im-internet.de/geschgehg/
- HinSchG: https://www.gesetze-im-internet.de/hinschg/
- BGH I ZR 136/17: https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&az=I%20ZR%20136/17
- BAG 2 AZR 547/05: https://juris.bundesarbeitsgericht.de/cgi-bin/rechtsprechung/document.py?Gericht=bag&Art=en&az=2%20AZR%20547/05
- Know-how-RL (EU) 2016/943: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016L0943

## Triage-Fragen bei Geschäftsgeheimnis-Mandat

Bevor die Schutzstrategie entwickelt wird, klaere:
1. Liegen "angemessene Geheimhaltungsmassnahmen" nach § 2 Nr. 1 lit. b GeschGehG vor (technisch UND organisatorisch)?
2. Ist die verletzte Information wirklich ein Geschaeftsgeheimnis oder bereits bekannte Branchen-Praxis?
3. Kommt § 5 GeschGehG (Whistleblowing-Ausnahme) oder § 36 HinSchG in Betracht?
4. Ist eine sofortige Sicherungsanordnung nach § 16 GeschGehG (Offenbarungsschutz im Verfahren) erforderlich?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `fachanwalt-gewrechts-ki-vo-50-genai`

**Fokus:** KI-generierte Inhalte auf gewerblichen Rechtsschutz prüfen wenn GenAI-Outputs Schutzrechte beruehren. Art. 50 KI-VO Transparenzpflichten §§ 2 7 UrhG KI-Autorschaft. Prüfraster: Urheberrechtsschutz KI-Autorschaft Kennzeichnungspflicht Art. 50 KI-VO Verletzungsrisiken. Output: Compliance-Memo Empfehlungen für KI-Nutzung. Abgrenzung: nicht für allgemeine KI-Governance.

## Mandantenfragen beim Kaltstart

1. Welches KI-System wird eingesetzt (ChatGPT, Midjourney, Sora, DALL-E, Stable Diffusion, Runway, unternehmensinternes LLM)?
2. Welcher Output-Typ wird erzeugt und wie eingesetzt — Text (Blog, Pressemitteilung), Bild (Produktfoto, Werbebanner), Video (Werbespot), Audio (Podcast-Stimme) oder Chatbot?
3. Wird der KI-Output unverändert verwendet, oder erfolgt redaktionelle Nachbearbeitung durch Mitarbeitende?
4. In welchem rechtlichen Kontext wird der Output eingesetzt (B2C-Werbung, B2B-Kommunikation, politische Werbung, Finanzdienstleistung, Pharmaziewerbung)?
5. Werden reale Personen in KI-generiertem Bild- oder Videomaterial dargestellt (Deep Fake-Risiko, §§ 22, 23 KUG, § 201a StGB)?
6. Ab wann soll die KI-Nutzung starten — Art. 50 KI-VO gilt ab 2.8.2026?
7. Liegt bereits ein Abmahnschreiben vor, oder soll präventive Compliance aufgebaut werden?
8. Werden KI-generierte Inhalte als urheberrechtlich geschützt vermarktet oder beansprucht?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| Art. 50 Abs. 1 KI-VO 2024/1689 | Anbieter von Chatbots müssen natürliche Personen informieren, dass sie mit einem KI-System interagieren |
| Art. 50 Abs. 2 KI-VO 2024/1689 | Anbieter generativer KI-Systeme: maschinenlesbare Markierung von Outputs (Wasserzeichen, kryptographische Signaturen, Metadaten); technische Standards durch Kommission |
| Art. 50 Abs. 4 KI-VO 2024/1689 | Verwender, die Deep Fakes erzeugen oder verbreiten, müssen Output als KI-generiert kennzeichnen; Ausnahme: offensichtlich künstlerischer oder satirischer Kontext |
| Art. 113 KI-VO | Anwendungszeitpunkt: Art. 50 gilt ab 2.8.2026 |
| Art. 99 KI-VO | Sanktionen: Bußgeld bis EUR 15 Mio. oder 3 % des weltweiten Jahresumsatzes (je nachdem, welcher Betrag höher ist) |
| § 5a UWG | Irreführung durch Unterlassen wesentlicher Informationen; KI-Herkunft als wesentliche Produkteigenschaft |
| § 5 Abs. 1 S. 2 Nr. 1 UWG | Irreführende Werbung: objektiv unrichtige oder täuschungsfähige Angaben über Eigenschaften |
| § 2 UrhG | Kein Urheberrechtsschutz für KI-Output: fehlendes Merkmal der persönlichen geistigen Schöpfung eines Menschen |
| §§ 22, 23 KUG | Recht am eigenen Bild: Deep Fakes mit realen Personen ohne Einwilligung unzulässig |
| § 201a StGB | Verletzung des höchstpersönlichen Lebensbereichs durch Bildaufnahmen; Deep-Fake-Reform ausstehend |
| § 7 UWG | Unzumutbare Belästigung: KI-generierte Massen-E-Mails ohne Einwilligung |
| Art. 22 DSGVO | Recht auf menschliche Überprüfung bei automatisierten Einzelentscheidungen |
| Art. 5 Abs. 1 lit. c DSGVO | Datenminimierung auch bei KI-Training-Inputs |
| § 3 GeschGehG | Reverse Engineering KI-Modelle: erlaubt sofern keine AGB-Beschränkung und keine Urheberrechtsverletzung |

## Leitentscheidungen und Regulatorische Quellen

| Quelle | Datum | Kernaussage |
|--------|-------|-------------|
| EU-KI-VO 2024/1689 (Amtsblatt L 2024/1689) | 12.07.2024 | In Kraft 1.8.2024; Art. 50 anwendbar 2.8.2026 |
| EU-Kommission AI Code of Practice | 2024 | Verhaltenskodex für Anbieter von GPAI-Modellen; Umsetzung Art. 53–55 KI-VO |
| C2PA-Standard v2.0 (Coalition for Content Provenance and Authenticity) | 2024 | Technischer Standard für Herkunftsnachweis von Mediendateien (Adobe, Microsoft, Sony, Nikon) |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

> **Hinweis zur Rechtsprechungslage:** Stand 05/2026 existiert keine veröffentlichte deutsche Leitentscheidung speziell zu Art. 50 KI-VO; die Norm gilt erst ab 02.08.2026. Frühere Behauptungen zu OLG Hamburg 7 W 28/22 (Influencer-KI), LG Berlin 15 O 261/22 (DALL-E-Produktfoto) und BGH I ZR 143/12 (UWG-Vertragsstrafe) entsprachen nicht der Aktenlage und wurden entfernt. Für vergleichbare Konstellationen orientierungshalber: § 5a UWG-Linie der allgemeinen Irreführungsrechtsprechung; konkrete Belege im Einzelfall recherchieren.

## Pflichten nach Output-Typ

| Output-Typ | Pflicht | Rechtsgrundlage | Ausnahme |
|-----------|---------|----------------|---------|
| Text (Blog, Pressemitteilung) | Maschinenlesbare Markierung (Metadaten, Unicode-Markers) | Art. 50 Abs. 2 KI-VO | Erhebliche redaktionelle Bearbeitung durch Mensch |
| Bild (Produktfoto, Werbebanner) | Maschinenlesbare Markierung (C2PA/Wasserzeichen) + ggf. sichtbarer Hinweis bei Verbraucher-B2C-Werbung | Art. 50 Abs. 2 + § 5a UWG | Offensichtlich künstlerisch |
| Video / Deep Fake mit realer Person | Kennzeichnung als KI-generiert zwingend (Untertitel, Anfangs-Disclaimer) | Art. 50 Abs. 4 KI-VO; §§ 22, 23 KUG | Einwilligung + offensichtlich Satire |
| Audio / Stimmen-Klon | Einwilligung der nachgeahmten Person + Kennzeichnung | Art. 50 Abs. 4 KI-VO; §§ 22, 23 KUG | Eigene Stimme verwendet |
| Chatbot / KI-Assistent | Sofort-Hinweis: "Sie kommunizieren mit einem KI-System" | Art. 50 Abs. 1 KI-VO | B2B bei ausdrücklicher Kenntnis der Gegenseite |
| Politische Werbung | Kennzeichnung + DSA Art. 26 (Werbetransparenz) | Art. 50 Abs. 4 KI-VO; DSA | Keine |

## Prüfschema Compliance Art. 50 KI-VO

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfpunkt | Norm | Maßnahme |
|---------|-----------|------|---------|
| 1 | KI-System ist generatives System i. S. KI-VO Anhang I? | KI-VO Anhang I | Systeminventar erstellen |
| 2 | Anbieter oder Verwender? | Art. 3 Nr. 3, 4 KI-VO | Anbieter: Art. 50 Abs. 2 (Wasserzeichen); Verwender: Art. 50 Abs. 4 (Deep Fake) |
| 3 | Output-Typ klassifizieren (Text/Bild/Video/Audio/Chatbot) | Art. 50 Abs. 1–4 | Pflichtenkatalog je Typ anwenden |
| 4 | Maschinenlesbare Markierung vorhanden? | Art. 50 Abs. 2 | C2PA-Standard, SynthID, EXIF-Metadaten |
| 5 | Sichtbarer Hinweis bei B2C-Werbung und Deep Fakes? | Art. 50 Abs. 4; § 5a UWG | Overlay-Text, Untertitel, Footer-Hinweis |
| 6 | Einwilligung realer Personen bei Gesicht/Stimme? | §§ 22, 23 KUG | Schriftliche Einwilligung vor Produktion |
| 7 | Kein Urheberrecht beansprucht? | § 2 UrhG | Interne Richtlinie: keine Schutzbehauptung für KI-Output |
| 8 | Subprozessor-Verträge mit KI-Anbieter | DSGVO Art. 28; Art. 50 Abs. 2 | SLA: Markierungspflicht des Anbieters sicherstellen |

## Compliance-Workflow

### Phase 1 — Bestandsaufnahme

```
Schritt 1: KI-System-Inventar
- Alle eingesetzten KI-Systeme: Produktname, Anbieter, Output-Typ, Verwendungskontext
- Trennung: Anbieter-Pflichten (Art. 50 Abs. 2) vs. Verwender-Pflichten (Art. 50 Abs. 4)

Schritt 2: Output-Kategorisierung
A = Nur maschinenlesbare Markierung (Text-intern, B2B-Reports)
B = Maschinenlesbar + sichtbarer Hinweis (B2C-Werbung, Produktbilder)
C = Zwingend menschenlesbare Kennzeichnung (Deep Fakes, Chatbots, politische Werbung)
```

### Phase 2 — Technische Umsetzung

```
Maschinenlesbare Markierung:
- C2PA-Standard: Adobe Content Credentials, Microsoft Azure AI Watermarking
- Google SynthID (Audio, Bild, Text, Video)
- EXIF/XMP-Metadaten (Bildproduktion)
- PNG-Chunks / ID3-Tags (Audio)

Sichtbare Kennzeichnung:
- Bild: Wasserzeichen-Overlay "KI-generiert / AI-generated"
- Video: Texteinblendung erste 5 Sekunden + Untertitel
- Audio: Ansage zu Beginn "Diese Stimme wurde durch KI erzeugt"
- Chatbot: Begrüßungstext "Sie kommunizieren mit einem KI-Assistenten"
- Text-Blog: Footer-Hinweis "Dieser Beitrag wurde mit KI-Unterstützung erstellt"
```

### Phase 3 — Vertragliche Absicherung

```
KI-Anbietervertrag (SLA-Ergänzung):
- Verpflichtung des Anbieters zur Bereitstellung maschinenlesbarer Markierung
 gemäß Art. 50 Abs. 2 KI-VO
- Indemnification-Klausel bei UWG-Abmahnung durch fehlendes Wasserzeichen
- DSGVO-Subprozessoren-Klausel Art. 28

Interne Richtlinie:
- Verbot, KI-Output als urheberrechtlich geschützt zu beanspruchen (§ 2 UrhG)
- Pflicht zur redaktionellen Kontrolle vor Veröffentlichung
- Freigabeprozess für Deep-Fake-Content (Einwilligung reale Person)
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — KI-VO Art. 50 Compliance für GenAI sicherstellen | Drei-Phasen-Workflow; Schriftsatzbausteine unten |
| Variante A — Mandant ist nur Nutzer kein Anbieter | Reduzierte Pflichten; Art. 50 Abs. 4 GenAI-Kennzeichnung pruefen |
| Variante B — Hochrisiko-KI zusaetzlich betroffen | Art. 9-16 KI-VO zusaetzlich pruefen; Konformitaetsbewertung noetig |
| Variante C — DeepFake-Generierung des Mandanten | Besonderes Risiko Art. 50 Abs. 2 und 3; Kennzeichnungspflicht strikt |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatz-Bausteine

### Modifizierte Unterlassungserklärung bei KI-Kennzeichnungs-Abmahnung

```
Modifizierte Unterlassungserklärung

Die [Schuldnerin] verpflichtet sich gegenüber der [Gläubigerin] für jeden Fall
der schuldhaften Zuwiderhandlung zur Zahlung einer Vertragsstrafe nach dem
Hamburger Brauch, folgende Handlung zu unterlassen:

Im geschäftlichen Verkehr gegenüber Verbrauchern [Bild/Video/Text]-Inhalte,
die mittels generativer KI-Systeme erstellt wurden, zu veröffentlichen, ohne
einen für Verbraucher wahrnehmbaren Hinweis auf die KI-Generierung anzubringen,
wenn dies geeignet ist, Verbraucher über die kommerzielle Herkunft oder
Eigenschaft des Inhalts zu täuschen (§ 5a UWG).

Klarstellend: Diese Erklärung gilt nicht für Inhalte, die nach Art. 50 Abs. 4
S. 2 KI-VO offensichtlich künstlerischen oder satirischen Zwecken dienen.

[Ort, Datum, Unterschrift]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

### Risikomatrix

| Konstellation | Risiko-Level | Primäre Norm | Sanktion |
|--------------|-------------|-------------|---------|
| B2C-Produktbild KI ohne Wasserzeichen | HOCH | § 5a UWG + Art. 50 Abs. 2 KI-VO | Abmahnung + Bußgeld bis EUR 15 Mio. |
| Deep Fake mit prominenter Person ohne Einwilligung | SEHR HOCH | §§ 22, 23 KUG + Art. 50 Abs. 4 KI-VO | Unterlassung + Schadensersatz + Strafbarkeit § 201a StGB |
| Chatbot ohne KI-Hinweis (B2C) | HOCH | Art. 50 Abs. 1 KI-VO | Bußgeld bis EUR 15 Mio. |
| KI-Output als urheberrechtlich geschützt beansprucht | MITTEL | § 5 UWG (irreführend); § 2 UrhG | Abmahnung; keine strafrechtliche Relevanz |
| Politische Werbung mit KI ohne Kennzeichnung | SEHR HOCH | Art. 50 Abs. 4 KI-VO + DSA Art. 26 | Doppelter Bußgeldtatbestand |
| Rein interne KI-Nutzung ohne externe Verbreitung | GERING | Keine Kennzeichnungspflicht nach außen | – |

## Beweislast

| Beweisthema | Beweislast | Beweismittel |
|------------|-----------|--------------|
| KI-Herkunft des Inhalts | Abmahnender (bei UWG-Verstoß) | Reverse-Engineering-Nachweis; Metadata-Analyse; C2PA-Signatur fehlt |
| Kennzeichnung vorhanden | Abgemahnter | C2PA-Zertifikat; Wasserzeichen-Nachweis; Screenshot des Disclaimers |
| Einwilligung reale Person (§§ 22, 23 KUG) | Verwender | Schriftliche Einwilligungsurkunde |
| Urheberrecht am KI-Output (Mensch als Schöpfer) | Kläger | Nachweis erheblicher kreativer Beisteuerung durch natürliche Person |
| Redaktionelle Kontrolle (Ausnahme Art. 50 Abs. 2) | Verwender | Interne Freigabe-Protokolle; Track-Changes-Dokumentation |

## Fristen

| Frist | Inhalt | Norm |
|-------|--------|------|
| Ab 2.8.2026 | Art. 50 KI-VO gilt; Bußgeldbewehrung aktiv | Art. 113 KI-VO |
| 6 Monate | Verjährung UWG-Unterlassungsanspruch ab Kenntnis | § 11 Abs. 1 UWG |
| 10 Tage (üblich) | Reaktionsfrist bei Abmahnung | § 13 UWG |
| ca. 4 Wochen | Selbstwiderlegungsrisiko bei einstweiliger Verfügung | § 12 UWG; Rspr. |
| Sofort | Chatbot-Hinweis bei Gesprächsbeginn | Art. 50 Abs. 1 KI-VO |

## Gegenargumente und Reaktion

| Gegenargument | Herkunft | Reaktion |
|--------------|---------|----------|
| "KI-VO gilt erst ab 2.8.2026 — heute noch kein Verstoß" | Abgemahnter | Bei § 5a UWG-Abmahnung: UWG gilt bereits; KI-Herkunft als wesentliche Information schon heute |
| "Inhalt wurde redaktionell bearbeitet — keine KI-Kennzeichnung nötig" | Verwender | Art. 50 Abs. 2: Ausnahme nur bei erheblicher Bearbeitung; Beweislast beim Verwender; Dokumentation erforderlich |
| "Satire / Kunst — Ausnahme Art. 50 Abs. 4 S. 2" | Verwender | Ausnahme eng: muss für Durchschnittsbetrachter offensichtlich sein; Zweifel gehen zu Lasten des Verwenders |
| "KI-Output ist urheberrechtlich geschützt" | Mandant/in | § 2 UrhG: nur persönliche geistige Schöpfung eines Menschen schutzfähig; KI erzeugt keinen Schutz; Gestaltungsspielraum des Prompters reicht nach herrschender Meinung nicht |
| "Bußgeld nur gegen Anbieter, nicht Verwender" | Mandant/in | Art. 50 Abs. 4: Verwender-Pflicht bei Deep Fakes; Art. 50 Abs. 1: Anbieter-Pflicht bei Chatbots; beide Ebenen gesondert prüfen |

## Streitwert und Kosten

**UWG-Abmahnung wegen fehlender KI-Kennzeichnung:**
- Streitwert: EUR 10.000–30.000 je nach Reichweite der Werbung.
- Anwaltsgebühren aus EUR 20.000: Abmahnung ca. EUR 1.029 netto; einstweilige Verfügung ca. EUR 2.000 netto.

**Bußgeld Art. 99 KI-VO:**
- Bis EUR 15 Mio. oder 3 % des weltweiten Jahresumsatzes (Obergrenze je nach Unternehmensgröße).
- Zuständige Behörde: Noch nicht abschließend bestimmt; erwartet werden nationale KI-Behörden (in Deutschland voraussichtlich BNetzA oder BfJ).

**Schadensersatz §§ 22, 23 KUG:**
- Immaterialschadensersatz bei Deep Fakes mit realen Personen: EUR 5.000–50.000 je nach Schwere.

## Strategische Empfehlung

| Situation | Empfehlung | Begründung |
|-----------|------------|-----------|
| Unternehmen startet KI-Werbung vor 2.8.2026 | Sofort C2PA + sichtbare Disclaimer einführen; § 5a UWG gilt schon | Präventive Compliance verhindert Abmahnung heute + Bußgeld ab 8/2026 |
| Abmahnung wegen fehlender KI-Kennzeichnung erhalten | Prüfen: liegt echter § 5a UWG-Verstoß vor? Missbräuchlichkeit § 8c UWG? | Frühzeitige Reaktion; ggf. modifizierte UE |
| Deep Fake mit bekannter Person geplant | Einwilligungsvertrag mit Person schließen; Kennzeichnung sicherstellen; Rechtsanwalt vor Produktion einschalten | Persönlichkeitsrecht + KI-VO kombiniert — Hochrisikokonstellation |
| KI-Output urheberrechtlich verwerten | Nur soweit erhebliche menschliche Schöpfung eingeflossen; Dokumentation des Schöpfungsprozesses | Fehlende Schutzfähigkeit kann Lizenzmodell gefährden |

## Anschluss-Skills

- `fachanwalt-gewerblicher-rechtsschutz-abmahnung-uwg` — UWG-Abmahnung wegen fehlender KI-Kennzeichnung
- `fachanwalt-gewrechts-geschgehg-kollisionen-nda-hinschg-urhg` — Urheberrecht und Geschäftsgeheimnisschutz bei KI-Training
- `fachanwalt-gewerblicher-rechtsschutz-markenanmeldung` — Markenrechtliche Fragen zu KI-generierten Logos
- `sanktions-compliance-pruefung` — Exportkontrolle bei KI-Technologieprodukten

## Quellen

- EU-KI-VO 2024/1689: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32024R1689
- Art. 50 KI-VO (Text): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32024R1689#d1e5400-1-1
- C2PA-Standard: https://c2pa.org/specifications/specifications/2.0/index.html
- EU AI Code of Practice: https://digital-strategy.ec.europa.eu/en/policies/ai-code-practice
- § 5a UWG: https://www.gesetze-im-internet.de/uwg_2004/__5a.html

---

> **Audit-Hinweis (27.05.2026):** BGH I ZR 94/13 (Hotelbewertungsportal, 19.03.2015) hatte keinen Bezug zu Art. 50 KI-VO und wurde aus dem Disclaimer entfernt. Das AZ wurde zuvor fälschlich als "Trojanisches Pferd" beschrieben; tatsächliches Thema ist die Haftung von Bewertungsportalen für Nutzereinträge (UWG, TMG). BGH I ZR 145/10 (Tigerkopf, 28.09.2011) war in diesem Skill nicht vorhanden; das AZ betrifft Deckelung von Abmahnkosten nach § 97a UrhG. Beide AZ haben keinen Bezug zu KI-VO Art. 50.

## 3. `faevvollzug-neu-001-ev-vollziehungscheck-dringlichkeit-titel-zus`

**Fokus:** EV-Vollziehungscheck: Dringlichkeit, Titel und Zustellung bei einstweiliger Verfügung im gewerblichen Rechtsschutz. § 929 ZPO Vollziehungsfrist, § 936 ZPO, § 12 UWG, Selbstzustellung, Parteibetrieb, Rechtsfolgen verspäteter Vollziehung.

### EV-Vollziehungscheck: Dringlichkeit, Titel und Zustellung

## Aufgabe
Dieser Skill prüft den EV-Vollziehungscheck bei einstweiligen Verfügungen im gewerblichen Rechtsschutz: Dringlichkeit erhalten, Titel korrekt erwirken, fristgerechte Vollziehung und Zustellung sicherstellen.

## Rechtsrahmen

| Norm | Inhalt |
|---|---|
| § 12 Abs. 1 UWG | Dringlichkeitsvermutung für einstweilige Verfügung im Lauterkeitsrecht |
| § 935 ZPO | Einstweilige Verfügung zur Sicherung eines Anspruchs |
| § 936 ZPO | Anwendung der Arrestervorschriften auf einstweilige Verfügungen |
| § 929 Abs. 2 ZPO | Vollziehungsfrist: 1 Monat ab Zustellung des Beschlusses an Antragsteller |
| § 929 Abs. 1 ZPO | Vollziehung des Arrestes (gilt über § 936 ZPO) |
| § 191 ZPO | Zustellung von Amts wegen vs. Parteibetrieb |
| § 192 ZPO | Parteizustellung: Beauftragung des Gerichtsvollziehers |
| § 922 Abs. 2 ZPO | Beschlussverfügung ohne mündliche Verhandlung |
| § 924 ZPO | Widerspruch gegen einstweilige Verfügung |

## Kritische Fristen und Dringlichkeit

### Dringlichkeit
- **UWG:** Gesetzliche Dringlichkeitsvermutung (§ 12 Abs. 1 UWG), aber **Selbstwiderlegung** bei zu langem Zuwarten nach Kenntnis des Verstoßes (Faustregel: ca. 4 Wochen, je nach Kammer kürzer).
- **Markenrecht / PatG / DesignG:** Keine gesetzliche Vermutung; Dringlichkeit ist darzulegen und glaubhaft zu machen (§ 920 ZPO).
- **Kenntniszeitpunkt** dokumentieren: Screenshot, E-Mail, Kaufbeleg mit Datum.

### Vollziehungsfrist § 929 Abs. 2 ZPO
- Frist: **1 Monat** ab Zustellung des Beschlusses an den Antragsteller.
- Vollziehungshandlung: Zustellung an den Antragsgegner (§ 929 Abs. 2 i.V.m. § 191, § 192 ZPO) oder Eintragung in Register (bei Immaterialgütern wenn möglich).
- Bei Versäumnis: Titel wird unwirksam, § 929 Abs. 2 ZPO.

## Checkliste EV-Vollziehung

| Schritt | Prüfpunkt | Ergebnis |
|---|---|---|
| 1 | Beschluss erhalten? Zustellungsdatum notieren | Fristbeginn § 929 Abs. 2 ZPO |
| 2 | Vollziehungsfrist berechnen (1 Monat) + Kalendernotiz | Fristablauf mit Puffer eintragen |
| 3 | Vollziehungsform wählen: Parteizustellung (§ 192 ZPO) oder Amtszustellung? | Parteibetrieb ist Standard |
| 4 | GV beauftragen (§ 192 ZPO) oder anwaltliche Zustellung gem. § 195 ZPO | Nachweis sichern |
| 5 | Zustellungsurkunde / Empfangsbekenntnis sichern | Für Vollziehungsnachweis |
| 6 | Dringlichkeit: Kenntnisdatum, keine Selbstwiderlegung? | Glaubhaftmachungsmittel bereithalten |
| 7 | Inhalt des Titels: Unterlassungsgebot klar formuliert? Ordnungsmittelhinweis? | Vollstreckbarkeit prüfen |
| 8 | Schutzschriftenregister gegnerisch hinterlegt? | [zssr.de](https://www.zssr.de) prüfen |

## Zustellungswege im Vergleich

| Weg | Rechtsgrundlage | Vorteil | Risiko |
|---|---|---|---|
| Gerichtsvollzieher (Parteibetrieb) | §§ 192, 194 ZPO | Sicher, protokolliert | Zeitaufwand; GV-Verfügbarkeit |
| Anwaltliche Zustellung | § 195 ZPO | Schnell bei kooperativer Gegenseite | Empfangsbekenntnis nötig |
| Einschreiben mit Rückschein | § 175 ZPO | Einfach | Nachweis bei Nichtabholung problematisch |
| Amtszustellung durch Gericht | § 168 ZPO | Kein Eigenaufwand | Langsam, keine Kontrolle |

## Dringlichkeits-Selbstwiderlegung vermeiden

- Sobald Verstoß bekannt: **sofort** dokumentieren (Screenshot, Kaufmuster, Datum).
- Abmahnung und Reaktionsfrist (1–2 Werktage bei Dringlichkeit) zügig setzen.
- Kein Zuwarten über die Kammergrenze hinaus (Hamburg: ca. 4 Wo; München: oft 3 Wo; Düsseldorf: teils strenger).
- Bei grenzüberschreitendem Sachverhalt: Gerichtsstand prüfen (§ 14 UWG; Art. 7 Nr. 2 EuGVVO).

## Einstieg
1. Wann wurde der Beschluss dem Antragsteller zugestellt? (Vollziehungsfristbeginn)
2. Welche Vollziehungshandlung ist geplant oder bereits erfolgt?
3. Liegt die Dringlichkeit noch vor oder droht Selbstwiderlegung?
4. Welches Gericht hat den Titel erlassen, welcher Gerichtsvollzieher ist zuständig?
5. Welcher Output wird gebraucht: Checkliste, Beauftragungsschreiben GV, Memo?

## Anschluss-Skills
- `faevvollzug-neu-002-parteibetrieb-und-gerichtsvollzieher-bei-unterlassungstiteln` – GV-Beauftragung im Detail.
- `faevvollzug-neu-004-vollstreckung-aus-unterlassungsverfuegung-ordnungsmittel` – Ordnungsgeldantrag nach Zuwiderhandlung.
- `workflow-fristen-und-risikoampel` – Fristenübersicht und Ampelbewertung.

## Quellenregel
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und Link zu [dejure.org](https://dejure.org) oder [openjur.de](https://openjur.de).
- Normen: [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- Keine BeckRS-, juris- oder Kommentar-Blindzitate aus Modellwissen.
- Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollständige Mandantenberatung.
- Keine eigenständige Fristberechnung ohne Kenntnis aller Zustelldaten.
- Keine Bewertung nicht belegter Zustellvorgänge.
