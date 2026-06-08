---
name: patg-verfuegung-beweislast-verletzungsklage
description: "Patg Verfuegung Beweislast Verletzungsklage im Plugin Fachanwalt Gewerblicher Rechtsschutz: prüft konkret PatG, Einstweilige Verfügung, Verletzungsklage. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Patg Verfuegung Beweislast Verletzungsklage

## Arbeitsbereich

**Patg Verfuegung Beweislast Verletzungsklage** ordnet den Fall über die tragenden Prüfungslinien: PatG, Einstweilige Verfügung, Verletzungsklage. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `spezial-patg-schriftsatz-brief-und-memo-bausteine` | PatG: Schriftsatz-, Brief- und Memo-Bausteine für Patentverletzungsklagen, Nichtigkeitsklagen BPatG, UPC-Verfahren, Berechtigungsanfragen, Lizenzverhandlungen und EPA-Einspruch. Normen §§ 9 und 139 ff. PatG, EPÜ, EPGÜ. |
| `spezial-verfuegung-beweislast-und-darlegungslast` | Einstweilige Verfügung: Beweislast und Darlegungslast. Glaubhaftmachung § 294 ZPO, Verfügungsanspruch und Verfügungsgrund, eidesstattliche Versicherung, Gegenglaubhaftmachung, sekundäre Darlegungslast, Beweismittel im Eilverfahren. |
| `spezial-verletzungsklage-sonderfall-und-edge-case` | Verletzungsklage: Sonderfälle und Edge Cases. Mittelbare Patentverletzung § 10 PatG, Erschöpfungseinwand § 24 MarkenG, Vorbenutzungsrecht § 12 PatG, Markenrechtliche Erschöpfung bei Reimport, fehlerhafte Schutzrechts-Übertragung, Designverletzung bei must-fit, Parallelimport. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `spezial-patg-schriftsatz-brief-und-memo-bausteine`

**Fokus:** PatG: Schriftsatz-, Brief- und Memo-Bausteine für Patentverletzungsklagen, Nichtigkeitsklagen BPatG, UPC-Verfahren, Berechtigungsanfragen, Lizenzverhandlungen und EPA-Einspruch. Normen §§ 9 und 139 ff. PatG, EPÜ, EPGÜ.

### PatG: Schriftsatz-, Brief- und Memo-Bausteine

## Aufgabe
Dieser Skill liefert Schriftsatz-Gerüste, Briefbausteine und Memo-Strukturen für patenrechtliche Mandate: Verletzungsklage, Nichtigkeitsklage, Berechtigungsanfrage und UPC-Verfahren.

## Rechtsrahmen

| Norm | Inhalt |
|---|---|
| § 9 PatG | Ausschließliches Recht: Herstellung, Anbieten, Inverkehrbringen, Benutzen |
| § 10 PatG | Mittelbare Patentverletzung |
| § 11 PatG | Schranken: private Nutzung, Forschungsprivileg, Vorbenutzungsrecht |
| § 13 PatG | Zwangslizenz (öffentliches Interesse) |
| § 139 PatG | Verletzungsklage: Unterlassung, Schadensersatz |
| § 140a PatG | Vernichtungsanspruch |
| § 140b PatG | Auskunftsanspruch |
| § 140c PatG | Vorlagenanspruch; Beweissicherungsklage |
| § 81 PatG | Nichtigkeitsklage / Beschränkungsverfahren vor BPatG |
| EPÜ Art. 99–105 | Einspruch gegen EP-Patent beim EPA |
| EPGÜ (UPC Agreement) | Unified Patent Court; Einheitspatent |
| ArbnErfG | Arbeitnehmererfindungen: Meldung, Vergütung, Inanspruchnahme |

## Schriftsatz-Gerüst: Patentverletzungsklage

```
An das Landgericht [Ort], Patentkammer

Klage

der [Klägerin GmbH], vertreten durch ...
– Klägerin –

gegen

[Beklagte GmbH], vertreten durch ...
– Beklagte –

wegen: Verletzung des deutschen Patents Nr. [Pat-Nr.], Az. [Az.]

KLAGEANTRÄGE

I. Die Beklagte wird verurteilt, es zu unterlassen, im Geltungsbereich
des DE-Patents Nr. [XX] [verletzte Handlung] zu [tun],
bei Meidung eines für jeden Fall der Zuwiderhandlung festzusetzenden
Ordnungsgeldes bis zu 250.000 €, ersatzweise Ordnungshaft.

II. Die Beklagte wird verurteilt, der Klägerin Auskunft zu erteilen über
Menge, Umsatz und Abnehmer der verletzenden Produkte.

III. Die Beklagte wird verurteilt, Schadensersatz zu zahlen; Höhe nach
Auskunft zu beziffern.

IV. Die Beklagte trägt die Kosten des Rechtsstreits.

SACHVERHALT

A. Schutzrecht der Klägerin
[Patentnummer, Anmeldedatum, Anspruch 1 und relevante Unteransprüche]

B. Verletzungshandlung
[Beschreibung: Produkt, Handlung, Datum, Marktort; Anlage: Testkauf / Produktdatenblatt]

C. Verletzungsanalyse
[Anspruchsmerkmale des Patentanspruchs; Subsumtion auf das angegriffene Produkt]

RECHTLICHE WÜRDIGUNG
§ 9 PatG: Herstellung / Anbieten / Inverkehrbringen des geschützten Gegenstands.

BEWEISANGEBOTE
[Zeuge, SV-Gutachten, Urkunden, Augenschein]
```

## Brief-Baustein: Berechtigungsanfrage

```
An [Adressat]

Berechtigungsanfrage betreffend Patent Nr. [XX]

Sehr geehrte Damen und Herren,

wir zeigen die Vertretung der [Mandantin] an.

Unsere Mandantin ist Inhaberin des deutschen Patents Nr. [XX] mit folgenden
Schutzansprüchen: [Kurzfassung Anspruch 1].

Wir haben festgestellt, dass Sie mit dem Produkt [Beschreibung] möglicherweise
von diesem Schutzrecht Gebrauch machen.

Wir bitten Sie, bis zum [Frist] mitzuteilen:
1. Auf welcher Rechtsgrundlage Sie die betreffende Handlung vornehmen.
2. Ob Sie bereit sind, eine Lizenzvereinbarung abzuschließen.

Sofern Sie keine Berechtigung nachweisen können, werden wir unsere Mandantin
über weitere Maßnahmen beraten.

[Unterschrift / Kanzlei]
```

## Memo-Baustein: Patentverletzungsanalyse

```
Vertraulicher Prüfvermerk: Patent [Nr.]

I. Schutzrecht
Patentinhaber: [Name]
Priorität: [Datum]
Anspruch 1: [Text]

II. Angegriffene Ausführungsform (AAF)
Produkt: [Bezeichnung]
Quelle: [Testkauf / Datenblatt / Messe]

III. Verletzungsanalyse (merkmalsweise)
Merkmal 1: [Anspruchstext] | AAF: [konkrete Ausführung] | Subsumtion: ✓ / ✗
Merkmal 2: ... | ... | ✓ / ✗
...

IV. Ergebnis
Alle Merkmale wortsinngemäß verwirklicht: Ja / Nein
Äquivalenzverletzung: Prüfen / Ja / Nein

V. Risiken
[Nichtigkeitsrisiko; Erschöpfungseinwand; Vorbenutzungsrecht § 12 PatG]

VI. Empfehlung
[Nächster Schritt: Abmahnung / EV / Klage / Verhandlung]
```

## ArbnErfG: Meldung und Inanspruchnahme

| Schritt | Norm | Frist |
|---|---|---|
| Erfindungsmeldung durch Arbeitnehmer | § 5 ArbnErfG | Unverzüglich |
| Inanspruchnahme durch Arbeitgeber | § 6 ArbnErfG | 4 Monate ab vollständiger Meldung |
| Vergütung (falls Inanspruchnahme) | § 9 ArbnErfG | Nach Richtlinien (Einzelerfindung) |
| Freigabe (falls keine Inanspruchnahme) | § 8 ArbnErfG | Automatisch nach 4 Monaten |

## Einstieg
1. Geht es um eine Verletzungsklage, Nichtigkeitsklage, Berechtigungsanfrage oder ArbnErfG?
2. Welches Patent ist betroffen (Nummer, Ansprüche, relevante Merkmale)?
3. Welche konkrete Verletzungshandlung wurde festgestellt?
4. Welcher Schriftsatztyp / Baustein wird benötigt?
5. Output: Klageschrift-Gerüst, Briefbaustein, Verletzungsanalyse-Memo?

## Anschluss-Skills
- `spezial-gewerblichen-tatbestand-beweis-und-belege` – Beweisführung Patent.
- `spezial-schadensersatz-abschlussprodukt-und-uebergabe` – Schadensersatz.
- `fachanwalt-gewerblicher-rechtsschutz-patent-nichtigkeitsklage` – Vollständiger Nichtigkeitsworkflow.

## Quellenregel
- PatG, ArbnErfG: [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- EPÜ: [epo.org](https://www.epo.org); UPC: [unified-patent-court.org](https://www.unified-patent-court.org).
- Rechtsprechung: [dejure.org](https://dejure.org), [bgh.de](https://www.bundesgerichtshof.de), [bundespatentgericht.de](https://www.bundespatentgericht.de).
- Keine BeckRS-, juris- oder Kommentar-Blindzitate aus Modellwissen.
- Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Was dieser Arbeitsgang nicht macht
- Keine technische Verletzungsanalyse ohne Patentschrift und Produktbeschreibung.
- Kein Ersatz für vollständige Mandantenberatung und Patentanwaltsbegutachtung.

## 2. `spezial-verfuegung-beweislast-und-darlegungslast`

**Fokus:** Einstweilige Verfügung: Beweislast und Darlegungslast. Glaubhaftmachung § 294 ZPO, Verfügungsanspruch und Verfügungsgrund, eidesstattliche Versicherung, Gegenglaubhaftmachung, sekundäre Darlegungslast, Beweismittel im Eilverfahren.

### Einstweilige Verfügung: Beweislast und Darlegungslast

## Aufgabe
Dieser Skill behandelt die Darlegungs- und Beweislast in einstweiligen Verfügungsverfahren: Glaubhaftmachung von Verfügungsanspruch und -grund, Mittel und Grenzen.

## Rechtsrahmen

| Norm | Inhalt |
|---|---|
| § 920 Abs. 2 ZPO | Glaubhaftmachung: Verfügungsanspruch und Verfügungsgrund |
| § 294 ZPO | Mittel der Glaubhaftmachung: Urkunden, eidesstattliche Versicherung, alle Beweismittel |
| § 935 ZPO | Einstweilige Verfügung: Sicherung des Anspruchs |
| § 940 ZPO | Einstweilige Verfügung zur Regelung eines Zustands |
| § 936 ZPO | Verweisung auf Arrestvorschriften |
| § 12 Abs. 1 UWG | Dringlichkeitsvermutung im Lauterkeitsrecht |
| § 286 ZPO | Freie Beweiswürdigung (Hauptsache) |
| § 294 Satz 2 ZPO | Sofortiger Beweis durch Glaubhaftmachungsmittel; keine Vereidigung nötig |

## Verfügungsanspruch – Darlegungsanforderungen

### Was muss dargelegt werden?

| Element | Inhalt | Beweismittel |
|---|---|---|
| Schutzrecht | Inhaber, Registernummer, Schutzbereich, Schutzfähigkeit | Registerauszug (DPMA/EUIPO) |
| Verletzungshandlung | Wann, wo, wie, durch wen | Screenshot, Testkauf, eV Mandant |
| Aktivlegitimation | Schutzrechtsinhaber oder bevollmächtigter Lizenznehmer | Registerauszug, Lizenzvertrag |
| Verletzungsform | Identisch / ähnlich; Verwechslungsgefahr; Tatbestandsmerkmale | Vergleichsmaterial |

### Glaubhaftmachungsgrad

- **Kein voller Beweis** nötig (§ 294 ZPO): überwiegende Wahrscheinlichkeit genügt.
- Eidesstattliche Versicherung des Mandanten als zentrales Instrument.
- Sachverständige können auch im EV-Verfahren eingesetzt werden, aber zeitkritisch.

## Verfügungsgrund – Darlegungsanforderungen

### Dringlichkeit

| Schutzrecht / Rechtsbereich | Dringlichkeit |
|---|---|
| UWG | Gesetzliche Vermutung § 12 Abs. 1 UWG; widerlegt bei Selbstwiderlegung |
| MarkenG, PatG, DesignG | Keine Vermutung; muss dargelegt werden: Kenntnisdatum, Erstmalige Verletzung, Eilbedürfnis |
| UrhG | Keine Vermutung; wie IP allgemein |

### Selbstwiderlegung vermeiden

- Dringlichkeit ist **widerlegt**, wenn der Antragsteller zu lange zugewartet hat nach Kenntnis vom Verstoß.
- Faustregel nach Kammer: Hamburg ~4 Wochen; München ~4 Wochen; Düsseldorf ~4 Wochen; Köln ~6 Wochen (Einzelfälle variieren).
- **Tipp:** Kenntniszeitpunkt genau dokumentieren; sofort handeln nach Kenntnis.

## Eidesstattliche Versicherung (eV) – Muster

```
Eidesstattliche Versicherung

Ich, [Name, Geburtsdatum], wohnhaft [Adresse], versichere an Eides statt
und erkläre folgendes:

1. [Mandant] betreibt [Unternehmen / Schutzrecht].

2. Am [Datum] habe ich auf der Website [URL] / in [Medium] folgende
 Verletzungshandlung festgestellt: [Beschreibung].

3. [Screenshot / Testkauf / Muster] ist als Anlage [X] beigefügt und
 gibt den Sachverhalt zutreffend wieder.

4. Von diesem Sachverhalt hatte ich erstmals am [Datum] Kenntnis.

5. Diese Erklärung gebe ich wahrheitsgemäß ab.

[Ort, Datum]
[Unterschrift]

Ich bin mir bewusst, dass eine vorsätzlich oder grob fahrlässig falsche
eidesstattliche Versicherung nach § 156 StGB strafbar ist.
```

## Gegenglaubhaftmachung durch Antragsgegner

| Strategie Antragsgegner | Ziel |
|---|---|
| Eigene eidesstattliche Versicherung | Sachverhalt bestreiten |
| Schutzschrift (ZSSR) | Gegenvortrag zu Verfügungsanspruch und -grund |
| Sofortiger Widerspruch | Mündliche Verhandlung erzwingen (§ 924 ZPO) |
| Einwand fehlender Dringlichkeit | Selbstwiderlegung der Antragstellerin darlegen |

## Sekundäre Darlegungslast

Bei bestimmten Sachverhalten (Verletzungsumfang, Herstellungsprozesse, Lieferkette) obliegt dem Antragsgegner eine sekundäre Darlegungslast, wenn er die Informationen exklusiv besitzt.

- BGH-Grundsatz: Wer über Informationen allein verfügt, muss substantiiert bestreiten oder darlegen.
- Anwendung im IP-Recht: Herkunft der Ware; Importmengen; technische Herstellungsdetails.

## Checkliste Darlegungs- und Beweislast EV

| Prüfpunkt | Erledigt? |
|---|---|
| Schutzrecht belegt (Registerauszug) | ☐ |
| Verletzungshandlung konkret dargelegt und datiert | ☐ |
| Kenntnisdatum dokumentiert (Selbstwiderlegungsschutz) | ☐ |
| Eidesstattliche Versicherung unterschrieben | ☐ |
| Anlagen nummeriert und dem Gericht übergeben | ☐ |
| Dringlichkeit dargelegt (UWG: Vermutung; sonst: positiv) | ☐ |
| Gegenglaubhaftmachung der Gegenseite antizipiert | ☐ |

## Einstieg
1. Liegt eine eigene eV vor oder muss sie noch aufgesetzt werden?
2. Ist das Kenntnisdatum dokumentiert?
3. Welche weiteren Glaubhaftmachungsmittel liegen vor (Testkauf, Screenshots)?
4. Hat die Gegenseite eine Schutzschrift hinterlegt?
5. Output: eV-Muster, Checkliste, Dringlichkeits-Memo, Gegenglaubhaftmachungs-Analyse?

## Anschluss-Skills
- `faevvollzug-neu-008-qualitaetsgate-vor-vollziehung` – Qualitätsgate.
- `spezial-gewerblichen-tatbestand-beweis-und-belege` – Beweismittelübersicht.
- `faevvollzug-neu-005-gegnerische-schutzschrift-auswerten` – Schutzschrift.

## Quellenregel
- ZPO: [gesetze-im-internet.de](https://www.gesetze-im-internet.de/zpo/); MarkenG, UWG: [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- Rechtsprechung: [dejure.org](https://dejure.org), [openjur.de](https://openjur.de), [bgh.de](https://www.bundesgerichtshof.de).
- Keine BeckRS-, juris- oder Kommentar-Blindzitate aus Modellwissen.
- Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Was dieser Arbeitsgang nicht macht
- Keine Bewertung der Dringlichkeit ohne Kenntnis des konkreten Kenntnisdatums.
- Kein Ersatz für vollständige Mandantenberatung.

## 3. `spezial-verletzungsklage-sonderfall-und-edge-case`

**Fokus:** Verletzungsklage: Sonderfälle und Edge Cases. Mittelbare Patentverletzung § 10 PatG, Erschöpfungseinwand § 24 MarkenG, Vorbenutzungsrecht § 12 PatG, Markenrechtliche Erschöpfung bei Reimport, fehlerhafte Schutzrechts-Übertragung, Designverletzung bei must-fit, Parallelimport.

### Verletzungsklage: Sonderfälle und Edge Cases

## Aufgabe
Dieser Skill behandelt die typischen Sonderfälle und Edge Cases bei Verletzungsklagen im gewerblichen Rechtsschutz: ungewöhnliche Einwände, Abgrenzungsprobleme und Randkonstellationen.

## Rechtsrahmen (Sonderfälle)

| Norm | Inhalt |
|---|---|
| § 10 PatG | Mittelbare Patentverletzung: Liefern von Mitteln |
| § 11 PatG | Schranken: Forschungsprivileg, private Nutzung, Vorbenutzungsrecht |
| § 12 PatG | Vorbenutzungsrecht: Benutzung vor Anmeldetag |
| § 24 MarkenG | Erschöpfung; Reimport; Parallelimport |
| § 3 DesignG | Schutzausschluss must-fit, must-match |
| § 4 Nr. 3 UWG | Ergänzender Leistungsschutz: wettbewerbliche Eigenart |
| Art. 5 EPÜ | Gebietsausnahmen für Luftfahrt, Forschungsschiffe |

## Edge Cases Patent

### Mittelbare Patentverletzung (§ 10 PatG)

**Tatbestand:** Liefern von Mitteln zur patentgeschützten Erfindung an Nicht-Berechtigte; Mittel bezieht sich auf wesentliches Element; Lieferer weiß oder hätte wissen müssen, dass Abnehmer Erfindung benutzt.

**Abgrenzung:** § 10 Abs. 2 PatG: Handelsübliche Erzeugnisse sind ausgenommen, außer bei gezielter Einwirkung auf Nutzung der Erfindung.

**Praxis:** Lieferant von Spezialchemikalien an jemanden, der damit patentiertes Verfahren anwendet.

### Vorbenutzungsrecht (§ 12 PatG)

**Tatbestand:** Wer am Anmeldetag des Patents das geschützte Verfahren / Erzeugnis im Inland bereits benutzte oder konkrete Vorkehrungen dazu getroffen hatte, darf weiter benutzen.

**Grenzen:** Vorbenutzungsrecht ist **nicht übertragbar** (außer mit dem Betrieb, § 12 Abs. 1 S. 2 PatG). Erweiterung der Benutzung über den ursprünglichen Umfang hinaus ist nicht gedeckt.

**Beweislast:** Vorbenutzungsberechtigter muss Vorbenutzung darlegen und beweisen.

### Forschungsprivileg (§ 11 Nr. 2 PatG)

Handlungen, die **ausschließlich** Versuchszwecken dienen, sind keine Verletzungshandlungen. Grenze: gewerbliche Nutzung der Forschungsergebnisse oder kommerzielle Herstellung.

## Edge Cases Marke

### Erschöpfung bei Reimport (§ 24 MarkenG)

**Grundsatz:** Erschöpfung tritt ein, wenn Ware mit Zustimmung des Markeninhabers **erstmals im EWR** in den Verkehr gebracht wurde.

**Sonderfall Reimport:** Reimport aus Drittland (z.B. USA → DE): **keine** Erschöpfung, auch wenn ursprünglich vom Markeninhaber exportiert.

**Sonderfall Grauware / Parallelimport:** Originale Ware aus einem anderen EWR-Land: Erschöpfung ja; aber: Umpacken ohne Zustimmung kann Erschöpfung beseitigen (EuGH „Boehringer Ingelheim vs. Swingward").

**EuGH-Linie:** Erschöpfung scheitert, wenn Markeninhaber berechtigte Gründe hat, weitere Benutzung zu untersagen (Art. 15 Abs. 2 UMV).

### Markenrechtsverletzung durch Metatags / Adwords

- BGH: Benutzung einer fremden Marke im HTML-Quelltext (Metatag) kann Verletzung sein.
- EuGH „Google France": Google AdWords – Nutzung als Keyword durch Mitbewerber ist Verletzung, wenn Herkunftshinweisfunktion beeinträchtigt.

## Edge Cases Design

### Must-fit / Must-match (§ 3 Abs. 1 Nr. 2 DesignG)

**Must-fit:** Merkmale, die mechanische Verbindung ermöglichen (z.B. Steckverbindungen), sind schutzausgeschlossen.

**Must-match:** Ersatzteile, die sichtbar sind und äußeres Erscheinungsbild bestimmen: Seit 2021 keine gesetzliche Ausnahme in DE; EUIPO-Praxis differiert. (Live-Prüfung empfohlen.)

**Praxisrelevanz:** Automobilersatzteile, Konsumgüter mit Ersatzteilen, modulare Systeme.

## Edge Cases UWG

### Ergänzender Leistungsschutz (§ 4 Nr. 3 UWG)

**Schutzvoraussetzungen:**
1. Wettbewerbliche Eigenart des Originals.
2. Nachahmung (identische Übernahme oder nachschaffende Übernahme).
3. Begleitende Umstände: Täuschung über Herkunft, Rufausbeutung oder Behinderung.

**Abgrenzung zu Designschutz:** Ergänzender Leistungsschutz setzt kein eingetragenes Recht voraus; schützt aber nur im Zusammenhang mit unlauterem Wettbewerb.

## Sonderproblem: Fehlerhafte Schutzrechts-Übertragung

- Klage durch ehemaligen Inhaber: Kein Anspruch mehr nach Übertragung.
- Klage durch Erwerber ohne vollständige Registrierung: Legitimation prüfen; Registerauszug aktuell.
- Konsequenz: Klageabweisung mangels Aktivlegitimation; Kosten des Klägers.

## Checkliste Edge Cases

| Prüfpunkt | Relevant? |
|---|---|
| Mittelbare Patentverletzung (§ 10 PatG): Lieferant von Mitteln? | ☐ |
| Vorbenutzungsrecht (§ 12 PatG): Nutzung vor Anmeldetag? | ☐ |
| Forschungsprivileg (§ 11 Nr. 2 PatG): Rein wissenschaftlich? | ☐ |
| Erschöpfungseinwand: EWR-Erstverkauf belegt? | ☐ |
| Must-fit / Must-match: Verbindungsmerkmal zwingend? | ☐ |
| Ergänzender Leistungsschutz: Begleitumstände? | ☐ |
| Aktivlegitimation: Registerübertragung vollständig? | ☐ |

## Einstieg
1. Welche Verletzungsklage oder welcher Einwand ist konkret?
2. Liegt einer der Edge Cases vor (mittelbare Verletzung / Erschöpfung / Vorbenutzung)?
3. Sind die relevanten Unterlagen vorhanden (Patent, Register, Testkauf)?
4. Output: Edge-Case-Analyse, Checkliste, Argumenationsmemo?

## Anschluss-Skills
- `spezial-markeng-risikoampel-und-gegenargumente` – Marken-Gegenargumente.
- `spezial-verfuegung-beweislast-und-darlegungslast` – Beweislast.
- `spezial-patg-schriftsatz-brief-und-memo-bausteine` – Patent-Schriftsätze.

## Quellenregel
- PatG, MarkenG, DesignG, UWG: [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- EuGH: [curia.europa.eu](https://curia.europa.eu); BGH: [bgh.de](https://www.bundesgerichtshof.de).
- Keine BeckRS-, juris- oder Kommentar-Blindzitate aus Modellwissen.
- Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Was dieser Arbeitsgang nicht macht
- Keine vollständige technische Verletzungsanalyse ohne Sachverständigen.
- Kein Ersatz für vollständige Mandantenberatung.
