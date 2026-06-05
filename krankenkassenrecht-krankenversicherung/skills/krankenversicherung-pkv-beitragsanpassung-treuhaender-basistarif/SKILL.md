---
name: krankenversicherung-pkv-beitragsanpassung-treuhaender-basistarif
description: "PKV Beitragsanpassung Treuhaender Basistarif: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# PKV Beitragsanpassung Treuhaender Basistarif

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **PKV Beitragsanpassung Treuhaender Basistarif** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-030-pkv-beitragsanpassung-treuhaender-begruendung-und-verjaeh` | PKV-Beitragserhöhungen nach § 203 VVG: Treuhänder-Zustimmung, formelle und materielle Anforderungen, BGH-Rechtsprechung und Rückforderungsverjährung. |
| `kv-031-pkv-basistarif-standardtarif-notlagentarif` | Auffangsysteme in der PKV: Basistarif (§ 152 VAG), Standardtarif, Notlagentarif (§ 153 VAG) – Voraussetzungen, Leistungsumfang und Wechselmöglichkeiten. |
| `kv-032-pkv-krankentagegeld-berufsunfaehigkeit-und-arbeitsunfaehi` | PKV-Krankentagegeld nach § 192 Abs. 5 VVG: Anspruchsvoraussetzungen, Arbeitsunfähigkeitsbegriff, Berufsunfähigkeitsabgrenzung und Leistungseinstellung. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **PKV Beitragsanpassung Treuhaender Basistarif**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-030-pkv-beitragsanpassung-treuhaender-begruendung-und-verjaeh`

**Fokus:** PKV-Beitragserhöhungen nach § 203 VVG: Treuhänder-Zustimmung, formelle und materielle Anforderungen, BGH-Rechtsprechung und Rückforderungsverjährung.

# PKV-Beitragsanpassung: Treuhänder, Begründung und Verjährung

## Skill-Zweck

PKV-Beiträge werden regelmäßig erhöht. Dieser Skill prüft, ob **Beitragsanpassungen formell und materiell wirksam** sind, analysiert die Treuhänderprüfung und klärt Rückforderungsansprüche bei unwirksamen Erhöhungen.

## Rechtlicher Rahmen

- **§ 203 VVG** – Beitragsanpassung (BA): Voraussetzungen, Treuhänder, Ankündigungspflicht
- **§ 178g VVG a.F.** – Altverträge (Übergangsrecht)
- **MB/KK 2009 § 8b** – Beitragsanpassungsklausel
- **§ 157 VAG** – Unabhängiger Treuhänder: Zustimmung erforderlich
- BGH IV ZR 255/17 – Grundsatzurteil 2021: formelle Begründungsanforderungen, Verjährung, Rückforderung
- BGH IV ZR 144/21 – Folgeurteil 2022: Substanzanforderungen für Mitteilung
- OLG Stuttgart 7 U 244/19 (Verjährung und Bereicherungsausgleich)

## Beitragsanpassungs-Prüfschema (BGH 2021)

| Prüfschritt | Inhalt | BGH-Maßstab |
|-------------|--------|-------------|
| Auslöser | Rechnungslegungsabweichung > 10 % (§ 203 Abs. 2 VVG) | Gesetzliche Schwelle |
| Treuhänder | Unabhängiger Treuhänder muss Erhöhung prüfen und zustimmen | § 157 VAG |
| Mitteilung | Versicherter muss vor Inkrafttreten informiert werden mit Begründung | § 203 Abs. 5 VVG |
| Begründung | Muss Auslöser und Anpassungsgrund verständlich nennen | BGH IV ZR 255/17 |
| Zeitpunkt | Anpassung frühestens zum nächsten Fälligkeitstermin nach 1 Monat Information | § 203 Abs. 5 VVG |

## Prüfprogramm

### Schritt 1 – Formelle Wirksamkeit
- Liegt eine schriftliche Mitteilung über Beitragsanpassung vor?
- Begründung: Welcher Auslöser wurde genannt (Leistungsausgaben, Sterblichkeit)?
- BGH IV ZR 255/17: Pauschale Begründung „gestiegene Kosten" reicht NICHT; konkreter Auslöser muss benannt werden
- Treuhänder-Zustimmung: nicht im Anschreiben erkennbar, aber Versicherer muss sie nachweisen können

### Schritt 2 – Materielle Wirksamkeit
- Berechnungsgrundlage: Ist die Höhe der Anpassung durch Versicherungsmathematik gedeckt?
- Treuhänder-Unabhängigkeit: Treuhänder darf nicht in dauerhafter Abhängigkeit vom Versicherer stehen
- Angemessenheit: offensichtliche Missverhältnisse können angefochten werden

### Schritt 3 – Rückforderungsanspruch
- Bei unwirksamer BA: Verjährung 3 Jahre nach Kenntnis (§ 195 BGB i.V.m. § 199 Abs. 1 BGB)
- BGH 2021: Kenntnis erst ab Urteilsdatum möglich → Verjährung neu beurteilen
- Rückforderung: § 812 BGB (ungerechtfertigte Bereicherung)
- Zeitraum: typisch 3 Jahre rückwirkend; ältere Erhöhungen verjährt

### Schritt 4 – Klage gegen PKV
- Zuständigkeit: Zivilgericht (AG bei < 5.000 €; LG bei ≥ 5.000 €)
- Streitwert: Summe aller unwirksamen Beitragserhöhungen + Zinsen
- Klasse Klagen: viele gleichartige Fälle → Vergleichsangebote des Versicherers beobachten
- Rückforderung + Feststellungsklage (Anpassung unwirksam) kombinieren

### Schritt 5 – Vergleich mit PKV
- Viele PKV haben nach BGH 2021 Vergleiche angeboten
- Vergleich prüfen: Abgeltung aller Ansprüche? Zu niedrig? Bindefrist?
- Vorher: vollständige Rückforderungsberechnung durchführen

## Typische Fallen

- **Unklare Verjährung vor BGH 2021**: Gerichte unterschiedlich; Einzelfallprüfung notwendig.
- **Mehrere Anpassungen pro Jahr**: Jede Anpassung einzeln auf Formfehler prüfen.
- **Bereicherungsausgleich**: Versicherer kann Gegenleistung (erhaltener Versicherungsschutz) aufrechnen; Nettoergebnis kleiner als rohe Rückforderung.
- **Neue Tarife nach Anpassung**: Wechsel in anderen Tarif (§ 204 VVG) als Alternative zur Klage.

## Output-Formate

- Beitragsanpassungs-Prüfprotokoll
- Rückforderungsberechnung (Tabelle)
- Klage auf Feststellung + Rückforderung (Muster)
- PKV-Auskunftsverlangen (Treuhänder, Unterlagen)
- Vergleichsbewertungs-Matrix

## Quellen

- [§ 203 VVG – Beitragsanpassung](https://www.gesetze-im-internet.de/vvg_2008/__203.html)
- [BGH IV ZR 255/17 – Leiturteil](https://www.bundesgerichtshof.de/DE/Entscheidungen/entscheidungen_node.html)
- [BGH IV ZR 144/21](https://www.bundesgerichtshof.de/DE/Entscheidungen/entscheidungen_node.html)
- [§ 157 VAG – Treuhänder](https://www.gesetze-im-internet.de/vag_2016/__157.html)
- [dejure.org § 203 VVG](https://dejure.org/gesetze/VVG/203.html)
- [PKV-Ombudsmann](https://www.pkv-ombudsmann.de)

## 2. `kv-031-pkv-basistarif-standardtarif-notlagentarif`

**Fokus:** Auffangsysteme in der PKV: Basistarif (§ 152 VAG), Standardtarif, Notlagentarif (§ 153 VAG) – Voraussetzungen, Leistungsumfang und Wechselmöglichkeiten.

# PKV: Basistarif, Standardtarif und Notlagentarif

## Skill-Zweck

Wer sich die PKV-Beiträge nicht leisten kann oder will, hat Optionen: **Basistarif, Standardtarif und Notlagentarif** bieten reduzierte Beiträge gegen eingeschränkte Leistungen. Dieser Skill klärt die Voraussetzungen, den Leistungsumfang und Wechselmöglichkeiten.

## Rechtlicher Rahmen

- **§ 152 VAG** – Basistarif: Leistungsumfang wie GKV; keine Risikoprüfung
- **§ 153 VAG** – Notlagentarif: bei Beitragsrückstand > 2 Monate
- **§ 193 Abs. 5 VVG** – Wechselrecht in Basistarif
- **§ 204 VVG** – Tarifwechsel innerhalb desselben Versicherers
- **§ 12 Abs. 1a VVG a.F.** – Standardtarif für Altverträge (vor 2009)
- Basistarif-Leistungsverordnung (BT-LV)
- BGH IV ZR 117/18 (Basistarif und Beitragsberechnung), BVerfG 1 BvR 2019/17

## Vergleich der Tarife

| Tarif | Beitrag | Leistung | Wechselmögl. | Personenkreis |
|-------|---------|----------|--------------|---------------|
| Basistarif | Max. GKV-Höchstbeitrag | GKV-Niveau | Jederzeit für Berechtigte | PKV-Versicherte ohne andere Option |
| Standardtarif | Begrenzt | Definierter Umfang | Nur für Altverträge | PKV-Versicherte vor 2009 |
| Notlagentarif | Niedrig | Nur Akutbehandlung | Automatisch bei Rückstand | Säumige PKV-Versicherte |
| Normaltarif | Marktpreis | Vollumfänglich | Nach Antragsprüfung | Neuverträge |

## Prüfprogramm

### Schritt 1 – Basistarif-Anspruch (§ 152 VAG)
- Wer hat Anspruch auf Wechsel in Basistarif?
 - PKV-Versicherte ohne anderweitigen Pflichtversicherungsanspruch
 - Versicherungspflichtige ohne KV-Schutz (Auffangpflichtversicherung)
 - GKV-Versicherte, die in PKV wechseln (nur Neuabschluss)
- Keine Risikoprüfung: PKV muss jeden aufnehmen
- Beitrag: max. allgemeiner GKV-Beitragssatz (14,6 %) * Beitragsbemessungsgrenze

### Schritt 2 – Leistungsumfang Basistarif
- GKV-ähnlich (Basisleis-Verordnung)
- KEIN Zusatzschutz (Einzel-/Zweibettzimmer, Chefarzt)
- Heilpraktiker und alternative Methoden: grundsätzlich ausgeschlossen
- Wichtig: Leistungen nach GKV-Standards, nicht nach GOÄ

### Schritt 3 – Notlagentarif (§ 153 VAG)
- Automatischer Wechsel bei Beitragsrückstand > 2 Monate
- Leistungen: nur Akutbehandlung, Schmerzen, Schwangerschaft (wie GKV-Ruhen)
- Beitrag: reduzierter Beitrag; aber Schulden laufen weiter
- Rückkehr: Begleichung aller Schulden inkl. Notlagentarifbeiträge

### Schritt 4 – Rückkehr aus Notlagentarif
- Vollständige Zahlung aller Rückstände + Notlagentarifbeiträge
- Übergang automatisch zurück in Normaltarif (oder Basistarif wenn beantragt)
- Sozialamt oder Grundsicherung: können Beitragsübernahme gewähren

### Schritt 5 – Standardtarif (Altverträge)
- Nur für PKV-Verträge abgeschlossen vor 1. Januar 2009
- Begrenzter Personenkreis: Versicherte ab 65 oder bei langer Mitgliedschaft
- Heute seltener relevant; Basistarif hat Standardtarif weitgehend verdrängt

## Typische Fallen

- **Basistarif und GOÄ**: Ärzte müssen für Basistarif-Patienten GKV-Vergütung akzeptieren (§ 75 Abs. 3a SGB V) – kein GOÄ-Honorar.
- **Rückkehr in Normaltarif aus Basistarif**: Neue Risikoprüfung kann verlangt werden; Zuschläge oder Ausschlüsse möglich.
- **Notlagentarif dauert an**: Ohne Bereinigung der Schulden kein Entkommen.
- **Wechsel und Wartezeiten**: Basistarif-Wechsel ohne neue Wartezeiten; aber Leistungseinschränkungen sofort.

## Output-Formate

- Basistarif-Wechselantrag
- Notlagentarif-Schuldenbereinigungsplan
- Leistungsvergleich Normal-/Basistarif
- Sozialamt-Übernahmeantrag (PKV-Beiträge)
- Rückkehr Normaltarif – Antrag

## Quellen

- [§ 152 VAG – Basistarif](https://www.gesetze-im-internet.de/vag_2016/__152.html)
- [§ 153 VAG – Notlagentarif](https://www.gesetze-im-internet.de/vag_2016/__153.html)
- [§ 193 VVG – Wechsel](https://www.gesetze-im-internet.de/vvg_2008/__193.html)
- [BVerfG 1 BvR 2019/17](https://www.bverfg.de/entscheidungen.html)
- [PKV-Verband Tarife](https://www.pkv.de)
- [dejure.org § 152 VAG](https://dejure.org/gesetze/VAG/152.html)

## 3. `kv-032-pkv-krankentagegeld-berufsunfaehigkeit-und-arbeitsunfaehi`

**Fokus:** PKV-Krankentagegeld nach § 192 Abs. 5 VVG: Anspruchsvoraussetzungen, Arbeitsunfähigkeitsbegriff, Berufsunfähigkeitsabgrenzung und Leistungseinstellung.

# PKV-Krankentagegeld: Berufsunfähigkeit und Arbeitsunfähigkeit

## Skill-Zweck

Das PKV-Krankentagegeld sichert das Einkommen bei Arbeitsunfähigkeit ab. Dieser Skill klärt **Anspruchsentstehung, Fortbestand und typische Einstellungsgründe** – insbesondere die gefährliche Schnittstelle zur Berufsunfähigkeit.

## Rechtlicher Rahmen

- **§ 192 Abs. 5 VVG** – Krankentagegeld: Voraussetzungen, Leistungsdauer
- **MB/KT 2009** – Musterbedingungen Krankentagegeld
- **§ 15 MB/KT 2009** – Ende der Leistungspflicht bei Berufsunfähigkeit
- **§ 4 Abs. 2 MB/KT** – Beginn der Leistung (Wartezeit)
- BGH IV ZR 305/14 (Krankentagegeld und Berufsunfähigkeit), BGH IV ZR 52/17
- BSG-Grundsätze zur Arbeitsunfähigkeit (teilweise analog anwendbar)

## Wichtige Begriffe

| Begriff | Inhalt |
|---------|--------|
| Arbeitsunfähigkeit | Vorübergehende Unfähigkeit, die zuletzt ausgeübte Tätigkeit auszuüben |
| Berufsunfähigkeit | Dauerhafte Unfähigkeit (> 6 Monate, i.d.R. 50 % Einschränkung) |
| Berufsunfähigkeit im KT-Vertrag | Löst Leistungsende aus (§ 15 MB/KT); auch wenn BU-Rente noch nicht bewilligt |

## Prüfprogramm

### Schritt 1 – Anspruchsentstehung
- Krankheitsbedingte Arbeitsunfähigkeit ärztlich bestätigt?
- Karenzzeit: Tarif sieht meist 42-tägigen Karenzzeitraum vor (ab dem Zeitpunkt)
- Wartezeit: 3 Monate nach Versicherungsbeginn für psychische Erkrankungen (§ 4 MB/KT)
- Tagesgeld-Betrag: vertraglich vereinbart (z.B. 50, 100 €/Tag)

### Schritt 2 – Fortbestand des Anspruchs
- Ärztliche Attestierung: regelmäßige AU-Bescheinigungen
- Verbesserungen: AU muss weiterhin vollständig vorliegen; Teilarbeitsfähigkeit kann Leistung reduzieren oder beenden
- Rückkehr in Beruf: sofortiges Leistungsende bei Aufnahme der Arbeit (auch stundenweise)

### Schritt 3 – Berufsunfähigkeits-Falle (§ 15 MB/KT)
- Wenn Versicherter voraussichtlich dauerhaft berufsunfähig: Leistung endet automatisch
- PKV kann Einstellung ankündigen wenn Prognose BU → ärztliche Gegendarstellung notwendig
- Wichtig: keine Gleichsetzung AU = BU; AU kann trotz drohender BU weiterbestehen
- BGH: Leistungsende erst wenn BU fest steht, nicht bei bloßer Möglichkeit

### Schritt 4 – Widerspruch gegen Leistungseinstellung
- PKV kündigt Einstellung an: sofort Gegengutachten des behandelnden Arztes
- Inhalt Gegengutachten: AU besteht weiterhin, Prognose nicht zwingend BU
- Eilantrag Zivilgericht: einstweilige Verfügung auf Weiterzahlung

### Schritt 5 – Koordinierung mit GKV-Krankengeld
- Selbstständige: haben kein GKV-Krankengeld → PKV-KT als alleinige Absicherung
- Angestellte mit PKV-Zusatztarif: GKV-Krankengeld zuerst; PKV-KT ergänzend
- Höchstgrenze: PKV-KT darf nicht über Nettoeinkommen hinausgehen (§ 4 Abs. 2 MB/KT)

## Typische Fallen

- **Berufsaufgabe während Krankentagegeld**: Wenn Selbstständiger seinen Betrieb aufgibt → Leistungsende wegen Wegfalls der Einkommensquelle.
- **Psychische Erkrankungen und Wartezeit**: 3-Monats-Wartezeit bei neu erkrankter psychischer Störung; vorher kein KT.
- **AU-Bescheinigung Lücke**: Wie GKV-Krankengeld: Lücke in Attestierung = Leistungsende.
- **BU-Rente und KT nebeneinander**: Nicht möglich; BU-Rente ersetzt KT; Übergangszeit wichtig für Planung.

## Output-Formate

- PKV-KT-Leistungsbrief (Anspruchsgeltendmachung)
- Widerspruch gegen BU-basierte Einstellung
- Ärztliches Gegengutachten-Briefing
- Einstweilige Verfügung Zivilgericht (Muster)
- Einkommensnachweis-Berechnung

## Quellen

- [§ 192 VVG – Krankentagegeld](https://www.gesetze-im-internet.de/vvg_2008/__192.html)
- [MB/KT 2009 – Musterbedingungen](https://www.pkv.de/service/broschueren/)
- [BGH IV ZR 305/14](https://www.bundesgerichtshof.de/DE/Entscheidungen/entscheidungen_node.html)
- [PKV-Ombudsmann](https://www.pkv-ombudsmann.de)
- [dejure.org § 192 VVG](https://dejure.org/gesetze/VVG/192.html)
- [BDA Berufsunfähigkeit](https://www.bda.de)
