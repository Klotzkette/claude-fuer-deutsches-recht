---
name: lease-maschinenleasing-abnahme-medizintechnik
description: "Lease Maschinenleasing Abnahme Medizintechnik: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lease Maschinenleasing Abnahme Medizintechnik

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Lease Maschinenleasing Abnahme Medizintechnik** im Plugin Leasingrecht Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lease-007-maschinenleasing-abnahme-wartung-und-stillstand` | Maschinenleasing: Abnahmeprozess, Wartungsverantwortung, Stillstandsrisiko, Mängelrechte und Rückgabe. |
| `lease-009-medizintechnik-leasing-regulatorische-wartung` | Medizintechnik-Leasing: MDR/IVDR-Anforderungen, Wartung, Betreiberverantwortung, Zulassung und Haftung bei Fehlfunktion. |
| `lease-012-verbraucherleasing-widerruf-und-pflichtangaben` | Verbraucherleasing: §§ 506–509 BGB, Pflichtangaben, Widerrufsrecht, Folgen fehlerhafter Angaben und Muster-Widerrufsbelehrung. |

## Arbeitsweg

Im Plugin Leasingrecht Praxis gilt für **Lease Maschinenleasing Abnahme Medizintechnik**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lease-007-maschinenleasing-abnahme-wartung-und-stillstand`

**Fokus:** Maschinenleasing: Abnahmeprozess, Wartungsverantwortung, Stillstandsrisiko, Mängelrechte und Rückgabe.

# Maschinenleasing: Abnahme, Wartung und Stillstand

## Zweck

Beim Maschinenleasing sind die technischen und rechtlichen Besonderheiten erheblich: Die Abnahme ist kein formaler Akt, sondern bestimmt Gefahrübergang und Gewährleistungsfristen. Wartungspflichten können den Restwert dramatisch beeinflussen. Stillstand bedeutet Umsatzverlust. Dieser Skill analysiert die rechtliche Struktur von der Abnahme bis zur Rückgabe.

## Rechtlicher Rahmen

- §§ 535 ff. BGB: Leasingvertrag als atypischer Mietvertrag
- §§ 433–480 BGB: Kaufvertragsrecht (Lieferant–LG); Sachmängelhaftung
- §§ 634–639 BGB: Werkvertragsrecht bei Maschinen mit Installationsleistung
- § 398 BGB: Abtretung der Gewährleistungsansprüche LG → LN
- §§ 305–310 BGB: AGB-Kontrolle
- EU-Maschinenverordnung (VO 2023/1230): Sicherheitsanforderungen; ersetzt MRL 2006/42/EG ab 2027
- §§ 340 ff. HGB: Handelsrechtliche Grundsätze bei gewerblichen LN

## Abnahme: Rechtliche Bedeutung

### Gefahrübergang
- Abnahme der Maschine durch LN = Gefahrübergang (§ 446 BGB analog)
- Vor Abnahme trägt LG das Risiko
- Nach Abnahme: LN trägt Untergangs- und Beschädigungsrisiko

### Abnahmeprotokoll
Empfohlener Inhalt:
- Maschinendaten (Typ, Seriennummer, Baujahr)
- Vollständigkeit (Zubehör, Werkzeuge, Handbücher, CE-Kennzeichnung)
- Funktionstest: Alle Betriebsmodi durchgelaufen?
- Mängel: Offen oder behoben?
- Unterschriften: LN und Lieferant
- Datum: Maßgeblich für Gewährleistungsfristen (2 Jahre ab Abnahme, § 438 I Nr. 3 BGB analog)

### Abnahmeverweigerung bei Mängeln
- LN kann Abnahme bei wesentlichen Mängeln verweigern
- Klausel: „Abnahme unter Vorbehalt" → Mängel notieren, Frist zur Behebung setzen
- Stillstand bis Mängelbeseitigung: Keine Leasingraten-Pflicht bei rechtmäßiger Abnahmeverweigerung? Umstritten; LN sollte Raten zahlen und Rückforderung geltend machen.

## Wartung und Instandhaltung

### Wer trägt Wartungsverantwortung?
**Finanzierungsleasing (Regelfall)**: LN ist für Wartung und Instandhaltung verantwortlich. Aus dem Leasingvertrag: Wartungspflicht des LN als Nebenleistungspflicht.

**Full-Service-Leasing**: LG oder Lieferant übernimmt Wartung gegen Pauschale.

### Wartungsnachweis
- Vertragsklausel: Häufig Nachweis durch Serviceheft oder digitales Wartungsprotokoll
- Fehlende Wartung → übermäßiger Verschleiß → LN haftet für Minderwert
- Steuerliche Abzugsfähigkeit: Wartungskosten als Betriebsausgabe des LN (da LN wirtschaftlicher Nutzer)

### Ersatzteile und Verbrauchsmaterialien
- Wer stellt bereit? Im Leasingvertrag regeln
- CE-Konformität bei Ersatzteilen: LN-Pflicht

## Stillstand und Nutzungsausfall

### Technischer Stillstand
- Maschine fällt aus: LN hat ggf. Ansprüche gegen Lieferant (abgetretene Mängelansprüche, § 398 BGB)
- LN kann LG informieren und auf Reparatur durch Lieferant drängen
- Leasingraten laufen weiter! Kein automatisches Ruhen der Ratenpflicht

### Stillstand wegen Mängeln vor Abnahme
- Noch nicht abgenommene Maschine → kein Ratenzahlungspflicht
- Nach Abnahme: LN zahlt Raten, macht Mängelrechte gegen Lieferant geltend

### Versicherung Betriebsunterbrechung
- Separate Betriebsunterbrechungsversicherung empfohlen
- Leasingvertrag meist nur Sachschadensversicherung (Feuer, Diebstahl)

## Rückgabe der Maschine

### Rückgabezustand
- Rückgabe in vertragsgemäßem Zustand
- Dokumentation: Zustandsprotokoll mit Fotos und Betriebsstundenzähler
- Verschleiß über vereinbartes Maß → Minderwert

### Demontage und Rücktransport
- Wer trägt Kosten? Im Vertrag regeln (oft LN)
- Fundament, Anschlüsse: Rückbaupflicht des LN?
- Beschädigungen bei Demontage: Haftungsklärung vorab

## Prüfprogramm

1. Abnahmeprotokoll vorhanden und vollständig? Mängel dokumentiert?
2. Gefahrübergang: Ab wann trägt LN das Risiko?
3. Abtretungsklausel: Kann LN direkt gegen Lieferant klagen?
4. Wartungsprotokoll: Belege für vertragsgemäße Wartung?
5. Stillstand: Wer haftet, laufen Raten weiter?
6. Rückgabe: Transportkosten, Demontage, Minderwertklausel

## Typische Fallen

- Abnahme ohne Protokoll → keine Beweissicherung für Ausgangszustand
- Mängelanzeige zu spät (§ 438 IV BGB analog) → Verjährung
- Wartungslücken → LG nimmt Minderwert bei Rückgabe
- Raten trotz Stillstand gezahlt ohne Rückforderung geltend zu machen

## Normen und Quellen

- § 446 BGB (Gefahrübergang): https://dejure.org/gesetze/BGB/446.html
- § 398 BGB (Abtretung): https://dejure.org/gesetze/BGB/398.html
- § 438 BGB (Sachmängelverjährung): https://dejure.org/gesetze/BGB/438.html
- EU-Maschinenverordnung (VO 2023/1230): https://eur-lex.europa.eu
- §§ 305–310 BGB: https://dejure.org/gesetze/BGB/305.html
- HGB §§ 343 ff.: https://www.gesetze-im-internet.de/hgb/__343.html
- openjur.de Maschinenleasing-Urteile: https://openjur.de

## Output-Formate

- **Abnahmeprotokoll-Vorlage**: Maschinenleasing mit Mängelliste
- **Wartungsnachweis-Checkliste**: Halbjährliche Wartungsdokumentation
- **Stillstands-Memo**: Rechtliche Optionen bei Maschinenausfall
- **Rückgabe-Checkliste**: Zustand, Betriebsstunden, Zubehör, Demontage

## 2. `lease-009-medizintechnik-leasing-regulatorische-wartung`

**Fokus:** Medizintechnik-Leasing: MDR/IVDR-Anforderungen, Wartung, Betreiberverantwortung, Zulassung und Haftung bei Fehlfunktion.

# Medizintechnik-Leasing: Regulatorische Anforderungen und Wartung

## Zweck

Medizinprodukte unterliegen neben dem allgemeinen Leasingrecht zusätzlichen Anforderungen der EU-Medizinprodukteverordnung (MDR 2017/745) und der Betreiberverordnung (MPBetreibV). Dieser Skill klärt, wer für Zulassung, Wartung und Betrieb verantwortlich ist und welche Folgen Pflichtverletzungen haben.

## Regulatorischer Rahmen

- **EU-MDR (VO 2017/745)**: Medizinprodukte Klasse I–III; Konformitätsbewertung, CE-Kennzeichnung, UDI
- **EU-IVDR (VO 2017/746)**: In-vitro-Diagnostika
- **MPG (bis 2021) / MPDG (ab 2021)**: Deutsches Medizinprodukterecht
- **MPBetreibV**: Pflichten des Betreibers (= Leasingnehmer in der Regel)
- **DGSV / DIN EN ISO**: Hygiene- und Wartungsstandards für Medizinprodukte

## Betreiberverantwortung (MPBetreibV)

Der **Betreiber** ist gemäß MPBetreibV diejenige Person oder Organisation, die das Medizinprodukt im Betrieb nutzt. Im Leasingverhältnis ist das typischerweise der **Leasingnehmer** (Krankenhaus, Arztpraxis, Labor).

### Kernpflichten des Betreibers (LN)
- Bestellung eines Beauftragten für Medizinproduktesicherheit (§ 83 MPDG ab 5 Produkten)
- Führung des Medizinproduktebuchs (Bestandsverzeichnis, §§ 13, 14 MPBetreibV)
- Sicherheitsüberprüfungen (STK) gemäß Herstellervorgabe und MPBetreibV
- Messtechnische Kontrollen (MTK) für bestimmte Gerätetypen
- Einweisung der Anwender (§ 10 MPBetreibV)
- Meldepflicht bei Vorkommnissen (§§ 85 ff. MPDG)

### Folgen von Pflichtverletzungen
- Ordnungswidrigkeit (§ 97 MPDG): Bußgeld bis 30.000 €
- Strafbarkeit bei Körperverletzung durch fehlerhafte Wartung (§§ 223, 229 StGB)
- Zivilrechtliche Haftung: LN haftet Patienten aus § 630a BGB (Behandlungsvertrag) und deliktisch (§ 823 BGB)

## Wartung im Leasingvertrag

### Wer ist wartungspflichtig?
- Leasingvertrag: Häufig LN (Betreiber) ist wartungspflichtig
- Full-Service-Leasing: LG/Hersteller übernimmt Wartung
- Wichtig: Unabhängig von vertraglicher Vereinbarung ist MPBetreibV zwingend → LN bleibt Betreiber

### Wartungsnachweis
- Jährliche Wartungsprotokolle (Serviceheft/CMMS)
- STK-Sticker auf Gerät
- Fehlende Wartung → Minderwert bei Rückgabe UND regulatorisches Risiko

## Zulassung und CE-Kennzeichnung

- Beim Abschluss des Leasingvertrags: Ist das Produkt CE-gekennzeichnet gemäß MDR?
- Für ältere Geräte: MDR-Übergangsfristen ausgelaufen? (MDR gilt ab 26.05.2021; Klasse III/IIb bis 2026)
- Wenn CE-Kennzeichnung wegfällt während Leasinglaufzeit: LN darf Gerät nicht mehr betreiben!

## Haftungsverteilung

| Sachverhalt | Haftung |
|---|---|
| Konstruktionsfehler Produkt | Hersteller (ProdHaftG) |
| Wartungsfehler durch LN | LN (MPBetreibV, § 823 BGB) |
| Lieferung mangelhafter Ware | Lieferant (abgetretener Anspruch) |
| Fehler durch fehlende Einweisung | LN (§ 10 MPBetreibV) |
| Vorkommnis nicht gemeldet | LN (MPDG §§ 85 ff.) |

## Insolvenz und Medizintechnik-Leasing

- §§ 108, 109 InsO: Insolvenzverwalter kann fortführen oder kündigen
- Besonderheit: Wenn das Gerät lebenserhaltend ist (z.B. Dialyse), kann Kündigung aus ethischen/rechtlichen Gründen faktisch unmöglich sein
- Praxis: Insolvenzverwalter sucht Käufer oder setzt auf Drittbetreiber

## Prüfprogramm

1. CE-Kennzeichnung nach MDR vorhanden und aktuell?
2. MPBetreibV-Pflichten: Medizinproduktebuch, STK, Einweisung, Meldesystem
3. Wartungsvertrag oder Eigenverantwortung? LG oder LN?
4. Vorkommnismeldung: Prozess implementiert?
5. Insolvenz: Gerät lebenserhaltend? Fortführungsverpflichtung faktisch?
6. EOL-Zulassung: Läuft MDR-Übergangsfrist ab während Leasingdauer?

## Typische Fallen

- MDR-Übergangsfrist während Leasinglaufzeit abgelaufen → CE weg → Betrieb illegal
- Keine Wartungsnachweise → regulatorisches Risiko + Minderwert bei Rückgabe
- Vorkommnis nicht gemeldet → MPDG-Bußgeld
- LN unterschreibt Leasingvertrag, aber vergisst MPBetreibV-Pflichten zu organisieren

## Normen und Quellen

- EU-MDR 2017/745: https://eur-lex.europa.eu
- MPDG (Medizinprodukterecht-Durchführungsgesetz): https://www.gesetze-im-internet.de/mpdg/
- MPBetreibV: https://www.gesetze-im-internet.de/mpbetreibv/
- ProdHaftG: https://www.gesetze-im-internet.de/prodhaftg/
- §§ 108, 109 InsO: https://www.gesetze-im-internet.de/inso/__108.html
- § 823 BGB: https://dejure.org/gesetze/BGB/823.html

## Output-Formate

- **Betreiberpflichten-Checkliste**: MDR/MPBetreibV für Leasingnehmer
- **Wartungsplan-Vorlage**: STK/MTK-Kalender für Medizintechnik
- **Vorkommnis-Meldungsschema**: MPDG §§ 85 ff.
- **Leasingvertrag-Check**: Wartungsklausel, Rückgabe, Minderwert

## 3. `lease-012-verbraucherleasing-widerruf-und-pflichtangaben`

**Fokus:** Verbraucherleasing: §§ 506–509 BGB, Pflichtangaben, Widerrufsrecht, Folgen fehlerhafter Angaben und Muster-Widerrufsbelehrung.

# Verbraucherleasing: Pflichtangaben und Widerruf

## Zweck

Leasingverträge mit Verbrauchern unterliegen besonderen Anforderungen nach §§ 506–509 BGB. Fehlende Pflichtangaben führen zu Nichtigkeit einzelner Klauseln oder des gesamten Vertrages. Das Widerrufsrecht kann weit über 14 Tage hinaus laufen, wenn die Widerrufsbelehrung fehlerhaft ist. Dieser Skill systematisiert Pflichtangaben, Widerrufsrecht und Rechtsfolgen.

## Anwendungsbereich §§ 506–509 BGB

### Verbraucherleasing als entgeltliche Finanzierungshilfe
§ 506 I BGB: „Entgeltliche Finanzierungshilfe" umfasst auch Leasingverträge, bei denen der Leasingnehmer nicht (oder nicht nur) zur Kaufpreiszahlung verpflichtet ist, aber das Objekt längerfristig nutzt und eine Gesamtlaufzeit vereinbart ist.

**Verbraucher** (§ 13 BGB): Natürliche Person, die nicht überwiegend gewerblich oder freiberuflich handelt.

**Unternehmer** (§ 14 BGB): Keine Anwendung der §§ 506–509 BGB.

### Abgrenzung § 506 zu § 491 BGB
- § 491 BGB: Verbraucherdarlehen (Kreditvergabe in Geld)
- § 506 BGB: Entgeltliche Finanzierungshilfe, einschließlich Leasing; Verweis auf §§ 491 ff. BGB
- Wichtig: § 506 III BGB enthält spezifische Anforderungen für Leasingverträge

## Pflichtangaben nach § 506 III BGB

Für Leasingverträge mit Verbrauchern müssen zwingend enthalten sein:
1. Art des Leasingvertrages
2. Name und Anschrift des Leasinggebers
3. Nettodarlehensbetrag (oder Nettoleasingwert/Anschaffungspreis des Objekts)
4. Gesamtbetrag (alle Zahlungen des LN summiert)
5. Laufzeit
6. Betrag, Anzahl und Fälligkeit der einzelnen Raten
7. Effektiver Jahreszins (§ 6 PAngV: Berechnung nach Annuitätenmethode)
8. Gesamtkosten
9. Hinweis auf Widerrufsrecht und Widerrufsfrist
10. Ggf. Restwert/Restwertgarantie
11. Ggf. Zusatzkosten (Versicherung, Wartung)

**Pflicht-Widerrufsinformation**: Entsprechend Anlage 7 oder 8 zu Art. 247 § 6 EGBGB

## Widerrufsrecht

### Frist
- Grundsatz: 14 Tage ab Vertragsschluss (§ 355 I BGB)
- Verlängerung: Wenn Pflichtangaben unvollständig oder Widerrufsinformation fehlerhaft → Widerruf weiterhin möglich (bis Heilung + 14 Tage)
- Maximum: 1 Jahr und 14 Tage (§ 356 b III BGB)

### Form des Widerrufs
- Textform (§ 126b BGB): E-Mail, Fax, Brief
- Keine Begründung erforderlich

### Folgen des Widerrufs
- Rückabwicklung: LN gibt Objekt zurück, LG erstattet Zahlungen
- Wertersatz: LN schuldet Wertersatz für tatsächliche Nutzung (§ 357 VII BGB)
- Kein Restwert: Restwertgarantie entfällt bei wirksamen Widerruf

## Rechtsfolgen fehlerhafter Pflichtangaben

### § 494 BGB (Fehlerfolge)
- Fehlende Pflichtangaben → Leasingvertrag kann nichtig sein (§ 494 I BGB)
- Ausnahme: Heilung durch tatsächlichen Empfang der Leistung (§ 494 II BGB)
- Nachholbarkeit bestimmter Angaben (§ 494 II, III BGB): Effektivzins, Gesamtbetrag

**Beispiel**: Fehlt der effektive Jahreszins → gilt kraft Gesetzes der gesetzliche Zinssatz (§ 494 II 5 BGB); LN zahlt weniger.

## Fernabsatzleasing

Verbraucherleasing über Internet/Telefon zusätzlich: §§ 312a ff. BGB (Fernabsatzverträge); Widerrufsrecht für Fernabsatz (14 Tage, § 356 BGB).

## Prüfprogramm

1. Ist der LN Verbraucher (§ 13 BGB)?
2. Liegen alle Pflichtangaben nach § 506 III BGB vor?
3. Widerrufsinformation korrekt (Anlage 7/8 EGBGB)?
4. Widerrufsfrist: Noch laufend?
5. Fehlerhafte Angabe: Welche Rechtsfolge (§ 494 BGB)?
6. Fernabsatz? Zusätzliche Anforderungen §§ 312 ff. BGB?

## Typische Fallen

- Effektiver Jahreszins falsch berechnet → LN schuldet nur gesetzlichen Zins
- Widerrufsbelehrung veraltet (EGBGB-Anlage nicht aktuell) → Widerruf noch möglich
- Restwertklausel im Vertrag, aber nicht als Pflichtangabe aufgeführt → Klausel nichtig
- Kein Hinweis auf Widerrufsrecht → Frist beginnt nicht zu laufen

## Normen und Quellen

- §§ 506–509 BGB: https://dejure.org/gesetze/BGB/506.html
- § 494 BGB (Fehlerfolge): https://dejure.org/gesetze/BGB/494.html
- § 355 BGB (Widerrufsrecht): https://dejure.org/gesetze/BGB/355.html
- Art. 247 EGBGB (Informationspflichten): https://www.gesetze-im-internet.de/egbgb/art_247.html
- § 6 PAngV (effektiver Jahreszins): https://www.gesetze-im-internet.de/pangv/__6.html
- §§ 312 ff. BGB (Fernabsatz): https://dejure.org/gesetze/BGB/312.html
- BGH XI ZR 59/17 (Widerruf Leasingvertrag): https://www.bgh.de

## Output-Formate

- **Pflichtangaben-Checkliste**: § 506 III BGB – alle 11 Punkte mit Beispielen
- **Widerrufsinformation-Muster**: Aktuelle Anlage 7 EGBGB
- **Fehlerfolgen-Tabelle**: Fehlende Angabe – Rechtsfolge – Heilung möglich?
- **Widerrufserklärung-Muster**: Für Verbraucher
