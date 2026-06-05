---
name: krankenversicherung-arbeitgeberzuschuss-pkv-entgeltabrechnung
description: "Arbeitgeberzuschuss PKV Entgeltabrechnung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Arbeitgeberzuschuss PKV Entgeltabrechnung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Arbeitgeberzuschuss PKV Entgeltabrechnung** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-040-arbeitgeberzuschuss-pkv-und-entgeltabrechnung` | AG-Zuschuss zur PKV nach § 257 SGB V: Höhe, Berechnung, Sozialversicherungsfreiheit, falsche Abrechnung und Rückforderungsrisiken. |
| `kv-041-rentner-krankenversicherung-der-rentner-kvdr` | Pflichtversicherung in der KVdR (§ 5 Abs. 1 Nr. 11 SGB V): Vorversicherungszeit, Beitragsbemessung, Versorgungsbezüge und Widerspruchsstrategien. |
| `kv-042-versorgungswerk-krankenversicherung-im-ruhestand` | Krankenversicherung für Mitglieder berufsständischer Versorgungswerke (Ärzte, Anwälte, Apotheker): Ausnahmen von KVdR, freiwillige GKV, PKV-Optionen. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Arbeitgeberzuschuss PKV Entgeltabrechnung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-040-arbeitgeberzuschuss-pkv-und-entgeltabrechnung`

**Fokus:** AG-Zuschuss zur PKV nach § 257 SGB V: Höhe, Berechnung, Sozialversicherungsfreiheit, falsche Abrechnung und Rückforderungsrisiken.

# Arbeitgeberzuschuss PKV und Entgeltabrechnung

## Skill-Zweck

Arbeitnehmer, die privat krankenversichert sind, haben Anspruch auf einen AG-Zuschuss zur PKV. Dieser Skill klärt **Berechnung, steuer- und sozialversicherungsrechtliche Behandlung und häufige Abrechnungsfehler**.

## Rechtlicher Rahmen

- **§ 257 SGB V** – AG-Zuschuss zur PKV: Hälfte des tatsächlichen Beitrags, max. Hälfte des fiktiven GKV-Anteils
- **§ 257 Abs. 2 SGB V** – Nachweis: Versicherer-Bescheinigung über PKV-Beitrag
- **§ 3 Nr. 62 EStG** – Steuerfreiheit des AG-Zuschusses
- **§ 1 Abs. 1 Nr. 4 SvEV** (Sozialversicherungsentgeltverordnung) – SV-Freiheit AG-Zuschuss
- **§ 28e SGB IV** – Beitragstragung bei sozialversicherungsfreien AN
- BSG B 12 KR 22/18 R (AG-Zuschuss PKV, Berechnung)

## AG-Zuschuss-Berechnung

| Parameter | Wert 2025 |
|-----------|-----------|
| Beitragssatz GKV (allgemeiner) | 14,6 % |
| Beitragsbemessungsgrenze | 5.512,50 €/Monat |
| Fiktiver AG-Anteil (7,3 %) bei BBG | 402,41 €/Monat |
| Max. AG-Zuschuss PKV | 402,41 €/Monat (wenn tatsächl. Beitrag ≥ 804,82 €) |
| Tatsächliche PKV < 804,82 €/Monat | AG zahlt 50 % des tatsächlichen Beitrags |

## Prüfprogramm

### Schritt 1 – Anspruchsvoraussetzungen
- Arbeitnehmer mit PKV?
- Kein Anspruch wenn PKV-Beitrag von AG als bKV getragen wird (Doppelerstattung vermeiden)
- Nachweis gegenüber AG: jährliche PKV-Beitragsbescheinigung

### Schritt 2 – Berechnung des Zuschusses
- PKV-Beitrag 600 €/Monat: AG zahlt 300 €
- PKV-Beitrag 900 €/Monat: AG zahlt 402,41 € (Deckelung bei fiktivem AG-Anteil)
- Pflegeversicherungszuschuss (§ 61 SGB XI): analog berechnen

### Schritt 3 – Steuer- und SV-Freiheit
- AG-Zuschuss steuerfrei (§ 3 Nr. 62 EStG): nur bis Höhe des fiktiven AG-Anteils
- Übersteigender Zuschuss: Sachbezug, zu versteuern
- SV-frei: AG-Zuschuss ist kein Arbeitsentgelt i.S.d. § 14 SGB IV

### Schritt 4 – Abrechnungsfehler erkennen
- Zu niedriger Zuschuss: AN prüft Lohnabrechnung; Differenz nachfordern (Verjährung 3 Jahre)
- Falscher Beitragsnachweis: PKV-Bescheinigung jährlich aktualisieren
- Elternzeit: AG-Zuschuss ruht grundsätzlich (kein Entgelt); aber individuelle Regelungen möglich

### Schritt 5 – Rückforderungsrisiken
- Überzahlter Zuschuss: AG kann unter engen Voraussetzungen zurückfordern
- Verjährung: 3 Jahre (§ 195 BGB)
- Wenn Arbeitnehmer GKV-versichert war trotz PKV-Zuschuss: Rückforderung möglich

## Typische Fallen

- **Beitragsbescheinigung nicht eingereicht**: AG muss keinen Zuschuss zahlen ohne Nachweis.
- **Zuschuss zu PKV-Krankentagegeld**: § 257 gilt für Krankenversicherung; Krankentagegeld ist separate Versicherung → kein Zuschuss-Anspruch.
- **Beitragserhöhung vergessen**: PKV erhöht Beitrag → neue Bescheinigung beim AG einreichen; sonst weiterhin alter Zuschuss.
- **Midijob-Grenze**: Bei Midijob-Beschäftigten (520–2.000 €) gelten besondere SV-Beitragstabellen; AG-Zuschuss-Berechnung anpassen.

## Output-Formate

- AG-Zuschuss-Berechnungsblatt
- PKV-Beitragsbescheinigung-Anforderungsschreiben
- Nachzahlungsantrag (Differenzforderung)
- Lohnabrechnung-Prüfprotokoll
- Elternzeit-Zuschusskalkulation

## Quellen

- [§ 257 SGB V – AG-Zuschuss PKV](https://www.gesetze-im-internet.de/sgb_5/__257.html)
- [§ 3 Nr. 62 EStG – Steuerfreiheit](https://www.gesetze-im-internet.de/estg/__3.html)
- [SvEV – Sozialversicherungsentgeltverordnung](https://www.gesetze-im-internet.de/svev/)
- [BSG B 12 KR 22/18 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 257 SGB V](https://dejure.org/gesetze/SGB_V/257.html)
- [GKV-Spitzenverband Beitragsrecht](https://www.gkv-spitzenverband.de)

## 2. `kv-041-rentner-krankenversicherung-der-rentner-kvdr`

**Fokus:** Pflichtversicherung in der KVdR (§ 5 Abs. 1 Nr. 11 SGB V): Vorversicherungszeit, Beitragsbemessung, Versorgungsbezüge und Widerspruchsstrategien.

# Rentner: Krankenversicherung der Rentner (KVdR)

## Skill-Zweck

Die Krankenversicherung der Rentner (KVdR) regelt die GKV-Pflichtmitgliedschaft im Rentenalter. Dieser Skill klärt **Vorversicherungszeit, Beitragsbemessung, Versorgungsbezüge und häufige Streitfragen**.

## Rechtlicher Rahmen

- **§ 5 Abs. 1 Nr. 11 SGB V** – Pflichtversicherung Rentner (KVdR)
- **§ 190 Abs. 11 SGB V** – Beginn der KVdR-Mitgliedschaft
- **§ 226 SGB V** – Beitragsbemessung bei Rentnern: Rente, Versorgungsbezüge, Arbeitseinkommen
- **§ 229 SGB V** – Versorgungsbezüge: Betriebsrenten, Direktversicherungen
- **§ 248 SGB V** – Beitragssatz für Rentner (hälftiger Beitrag; keine AG-Hälftetragung)
- **§ 256 SGB V** – Abzug der Beiträge durch Rentenversicherungsträger
- BSG B 12 KR 10/17 R (KVdR-Vorversicherungszeit), BSG B 12 KR 14/14 R (Versorgungsbezüge)

## KVdR-Vorversicherungszeit

| Zeitraum | Mindestanteil GKV |
|----------|------------------|
| 2. Hälfte des Erwerbslebens | 9/10 GKV-versichert |
| Berechnung | 2. Hälfte = Hälfte aller Beschäftigungsjahre; GKV-Zeiten inkl. freiwillig, Familienversicherung |
| Fehlerquelle | Zeiten in PKV zählen nicht; Zeiten als Selbstständiger ohne GKV zählen nicht |

## Prüfprogramm

### Schritt 1 – Vorversicherungszeit berechnen
- Gesamtes Erwerbsleben feststellen (Beginn bis Rentenantritt)
- 2. Hälfte identifizieren
- GKV-Zeiten in der 2. Hälfte: Pflicht + freiwillig + Familienversicherung
- Mindestens 9/10 = 90 % der 2. Hälfte in GKV?

### Schritt 2 – Anspruchsprüfung und Antrag
- Gleichzeitig Rentenantrag gestellt? (Rentenantrag löst KVdR-Prüfung aus)
- Kasse prüft Vorversicherungszeit automatisch
- Ablehnung: Widerspruch mit eigener Berechnung und Nachweisen (Sozialversicherungsverlauf)

### Schritt 3 – Beitragsbemessung (§ 226 SGB V)
- Beitragspflichtig: Rente + Versorgungsbezüge + Arbeitseinkommen
- Nicht beitragspflichtig: Wohngeld, Grundsicherung, steuerfreie Kapitalleistungen (außer § 229)
- Beitrag: allgemeiner Beitragssatz (14,6 %) + Zusatzbeitrag; Hälftetragung: Rentner 50 %, Rentenversicherungsträger 50 %

### Schritt 4 – Versorgungsbezüge (§ 229 SGB V)
- Beitragspflichtig: Betriebsrente, Direktversicherung, Pensionskasse
- Freibetrag 2025: 187,25 €/Monat
- Kapitalzahlungen aus Direktversicherungen: auf 10 Jahre verteilt (120 Monate) → Monatsbetrag beitragspflichtig
- BSG: auch Einmalzahlungen beitragspflichtig

### Schritt 5 – Kein KVdR-Anspruch: freiwillige Versicherung
- Vorversicherungszeit nicht erfüllt: freiwillige Versicherung (§ 9 SGB V) möglich
- Beitrag höher: Mindestbemessungsgrundlage § 240 SGB V
- Keine Hälftetragung durch Rentenversicherungsträger

## Typische Fallen

- **PKV-Zeiten als Lücken**: Zeiten in der PKV zählen nicht für KVdR-Vorversicherung → führt bei Wechseln in KVdR-Verlust.
- **Familienversicherungszeiten**: Zeiten als Familienmitglied werden angerechnet; oft unterschätzt.
- **Minijob-Rente**: Geringfügige Beschäftigung als Rentner kann Beitrag erhöhen (§ 226 Abs. 1 Nr. 3 SGB V).
- **Frührentner**: KVdR erst bei gesetzlicher Rente; Frührentner aus privaten Quellen nicht automatisch KVdR.

## Output-Formate

- Vorversicherungszeitberechnung (Tabelle)
- Widerspruch gegen KVdR-Ablehnung
- Versorgungsbezüge-Beitragsberechnung
- Kapitalleistungs-Monatsbeitragsberechnung
- KVdR vs. freiwillig Versichert – Kostenvergleich

## Quellen

- [§ 5 SGB V Nr. 11 – KVdR](https://www.gesetze-im-internet.de/sgb_5/__5.html)
- [§ 229 SGB V – Versorgungsbezüge](https://www.gesetze-im-internet.de/sgb_5/__229.html)
- [§ 226 SGB V – Beitragsbemessung Rentner](https://www.gesetze-im-internet.de/sgb_5/__226.html)
- [BSG B 12 KR 10/17 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [Deutsche Rentenversicherung](https://www.deutsche-rentenversicherung.de)
- [dejure.org § 229 SGB V](https://dejure.org/gesetze/SGB_V/229.html)

## 3. `kv-042-versorgungswerk-krankenversicherung-im-ruhestand`

**Fokus:** Krankenversicherung für Mitglieder berufsständischer Versorgungswerke (Ärzte, Anwälte, Apotheker): Ausnahmen von KVdR, freiwillige GKV, PKV-Optionen.

# Versorgungswerk: Krankenversicherung im Ruhestand

## Skill-Zweck

Mitglieder berufsständischer Versorgungswerke (Ärzte, Rechtsanwälte, Apotheker, Steuerberater) sind oft von der gesetzlichen Rentenversicherung befreit. Im Rentenalter fehlt dann der KVdR-Anspruch. Dieser Skill klärt die **Krankenversicherungsoptionen im Ruhestand**.

## Rechtlicher Rahmen

- **§ 6 SGB VI** – Befreiung von Rentenversicherungspflicht für Versorgungswerks-Mitglieder
- **§ 5 Abs. 1 Nr. 11 SGB V** – KVdR setzt gesetzliche Rente voraus → Versorgungswerks-Rentner grundsätzlich nicht KVdR-berechtigt
- **§ 9 SGB V** – Freiwillige Versicherung: Option für Versorgungswerks-Rentner
- **§ 240 SGB V** – Mindestbemessungsgrundlage freiwillig Versicherter
- **§ 192 VVG** – PKV als Alternative
- BSG B 12 KR 8/16 R (Versorgungswerk und KVdR)

## Optionen-Matrix Versorgungswerk-Rentner

| Option | Kosten | Voraussetzung | Leistungsumfang |
|--------|--------|--------------|-----------------|
| Freiwillige GKV (§ 9 SGB V) | Mindestbeitrag § 240 | Nachweis Ruhegehalt-Einkommen | GKV-Leistungen |
| PKV (fortlaufend aus Erwerbszeit) | Marktprämie (altersbedingt hoch) | Bestehende PKV fortführen | PKV-Tarif |
| PKV-Basistarif | Max. GKV-Höchstbeitrag | Jederzeit beantragbar | GKV-ähnlich |
| Beihilfe (nur Beamte) | Rest nach Beihilfe | Beamtenstatus | Nach BBhV |

## Prüfprogramm

### Schritt 1 – KVdR-Berechtigung ausschließen
- Besteht Anspruch auf gesetzliche Rente aus DRV? (trotz Versorgungswerks-Mitgliedschaft manchmal Kleinstansprüche)
- Vorversicherungszeit in 2. Hälfte des Erwerbslebens GKV erfüllt?
- Wenn KVdR-Anspruch besteht: günstiger als freiwillige GKV

### Schritt 2 – Freiwillige GKV als Option
- 3-Monats-Beitrittsfrist nach Beendigung des Arbeitsverhältnisses (§ 9 Abs. 2 Nr. 1 SGB V)
- Oder: nach Ende einer anderweitigen Krankenversicherung
- Beitrag: nach tatsächlichem Einkommen (Ruhegehalt des Versorgungswerks)
- Mindestbemessungsgrundlage 2025: 1.178,33 €/Monat

### Schritt 3 – PKV im Rentenalter fortführen
- Bestehende PKV: beibehalten; hohe Beiträge im Alter, aber Altersrückstellungen helfen
- Tarifwechsel (§ 204 VVG): in günstigeren Tarif wechseln
- Basistarif als Rückfalllösung wenn Beiträge nicht mehr tragbar

### Schritt 4 – Steuerliche Überlegungen
- PKV-Beiträge im Rentenalter: bis Vorsorgehöchstbetrag steuerlich absetzbar (§ 10 Abs. 1 Nr. 3 EStG)
- GKV-Beiträge freiwillig: ebenfalls absetzbar
- Kapitaleinkünfte im Rentenalter: erhöhen ggf. freiwilligen GKV-Beitrag

### Schritt 5 – Koordination Versorgungswerk und GKV
- Versorgungswerk-Rente + freiwillige GKV: Beitrag aus Versorgungswerk-Rente + weiteren Einkünften
- Kein Zuschuss der Rentenversicherung (nur bei KVdR)
- Antrag freiwillige GKV bei gewählter Krankenkasse; Kassenwahlrecht besteht (§ 175 SGB V)

## Typische Fallen

- **Beitrittsfrist versäumt**: Wer nach Berufsende zu lange wartet, verliert freiwilligen GKV-Eintritt.
- **Kleinstanspruch DRV**: Auch minimale DRV-Rente kann KVdR-Berechtigung auslösen – Kontenklärung vor Rentenantritt.
- **PKV-Beiträge im Alter unterschätzt**: Ohne Altersrückstellungen können Beiträge erheblich steigen.
- **Familienversicherung Ehegatten**: GKV-freiwillig versicherter Versorgungswerks-Rentner kann Ehegatte kostenfrei mitversichern.

## Output-Formate

- KVdR-Prüfberechnung (Vorversicherungszeit)
- Freiwillige GKV-Antrag
- GKV vs. PKV Kostenvergleich (Ruhestand)
- Tarifwechselantrag PKV § 204 VVG
- Steueroptimierungsübersicht KV-Beiträge

## Quellen

- [§ 5 SGB V – KVdR](https://www.gesetze-im-internet.de/sgb_5/__5.html)
- [§ 9 SGB V – Freiwillige Versicherung](https://www.gesetze-im-internet.de/sgb_5/__9.html)
- [§ 6 SGB VI – Befreiung RV](https://www.gesetze-im-internet.de/sgb_6/__6.html)
- [§ 240 SGB V – Mindestbeitrag](https://www.gesetze-im-internet.de/sgb_5/__240.html)
- [BSG Versorgungswerk-Rechtsprechung](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 9 SGB V](https://dejure.org/gesetze/SGB_V/9.html)
