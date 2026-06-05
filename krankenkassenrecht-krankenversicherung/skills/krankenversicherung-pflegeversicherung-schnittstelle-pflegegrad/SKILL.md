---
name: krankenversicherung-pflegeversicherung-schnittstelle-pflegegrad
description: "Pflegeversicherung Schnittstelle Pflegegrad: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Pflegeversicherung Schnittstelle Pflegegrad

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Pflegeversicherung Schnittstelle Pflegegrad** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-046-pflegeversicherung-schnittstelle-pflegegrad` | Schnittstelle GKV und GPV: Pflegegrad-Einstufung (SGB XI), Krankenbehandlung vs. Pflege, Hilfsmittel, Pflegehilfsmittel und Finanzierungsabgrenzung. |
| `kv-047-hospiz-palliativversorgung-und-sapv` | GKV-Leistungen für sterbende Menschen: Hospizversorgung (§ 39a SGB V), SAPV (§ 37b SGB V), Zuzahlungsbefreiung und Versorgungskoordination. |
| `kv-048-krankenkassenregress-behandlungsfehler-und-erstattung` | Regressansprüche der GKV gegen Leistungserbringer bei Behandlungsfehlern (§ 116 SGB X): Voraussetzungen, Höhe, Verjährung und Verhältnis zum Patientenanspruch. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Pflegeversicherung Schnittstelle Pflegegrad**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-046-pflegeversicherung-schnittstelle-pflegegrad`

**Fokus:** Schnittstelle GKV und GPV: Pflegegrad-Einstufung (SGB XI), Krankenbehandlung vs. Pflege, Hilfsmittel, Pflegehilfsmittel und Finanzierungsabgrenzung.

# Pflegeversicherung: Schnittstelle Pflegegrad

## Skill-Zweck

GKV und Pflegeversicherung überschneiden sich bei Hilfsmitteln, Häuslicher Krankenpflege und Reha. Dieser Skill klärt die **Leistungsabgrenzung zwischen § 37 SGB V und SGB XI** und löst Zuständigkeitskonflikte.

## Rechtlicher Rahmen

- **§ 14 SGB XI** – Pflegebedürftigkeit: Pflegegradmaßstab (NBA)
- **§ 36 SGB XI** – Pflegesachleistung: Körperpflege, Mobilität, Hauswirtschaft
- **§ 40 SGB XI** – Pflegehilfsmittel
- **§ 37 SGB V** – Häusliche Krankenpflege: Behandlungspflege, Grundpflege
- **§ 38 SGB V** – Haushaltshilfe GKV
- **§ 33 SGB V** – Hilfsmittel GKV (vs. § 40 SGB XI Pflegehilfsmittel)
- **§ 13 Abs. 2 SGB XI** – Nachrang Pflegeversicherung gegenüber anderen Leistungsträgern
- BSG B 3 P 7/05 R (Abgrenzung GKV/PV), BSG B 1 KR 26/16 R

## Abgrenzungsmatrix GKV vs. PV

| Leistung | GKV (SGB V) | PV (SGB XI) |
|----------|-------------|-------------|
| Behandlungspflege | § 37 Abs. 2 SGB V: bei Krankheit | Nachrangig |
| Grundpflege (Körperpflege) | Nein (außer häusliche Krankenpflege) | § 36 SGB XI |
| Hauswirtschaftliche Versorgung | § 38 SGB V (eng) | § 36 SGB XI |
| Hilfsmittel (Rollstuhl, Prothese) | § 33 SGB V | – |
| Pflegehilfsmittel (Pflegebett, Inkontinenzartikel) | – | § 40 SGB XI |
| Wohnraumanpassung | Nein | § 40 Abs. 4 SGB XI |
| Reha | § 40 SGB V | Nein (nachrangig) |

## Prüfprogramm

### Schritt 1 – Pflegegrad feststellen
- Antrag beim zuständigen Pflegekassenträger (bei GKV meist gleiche Organisation)
- Begutachtung durch MD (Medizinischer Dienst): NBA-Systematik
- Pflegegrade 1–5: je höher, desto mehr Leistungen

### Schritt 2 – Behandlungspflege vs. Grundpflege
- Behandlungspflege (§ 37 Abs. 2 SGB V): ärztliche angeordnete Behandlungsmaßnahmen (Verbandwechsel, Insulin, Medikamentengabe) → GKV
- Grundpflege: Waschen, Anziehen → PV
- Kombination: wenn beides nötig → beide Träger müssen koordinieren

### Schritt 3 – Hilfsmittel vs. Pflegehilfsmittel
- Hilfsmittel § 33 SGB V: Ausgleich einer Behinderung (Rollstuhl, Hörgerät) → GKV
- Pflegehilfsmittel § 40 SGB XI: Erleichterung der Pflege (Pflegebett, Greifzange, Einmalhandschuhe) → PV
- Graubereich: Inkontinenzartikel → § 40 SGB XI (wenn vorwiegend Pflegecharakter)

### Schritt 4 – Nachrangigkeit PV (§ 13 SGB XI)
- PV ist nachrangig gegenüber GKV, Unfallversicherung und anderen Trägern
- Kasse muss zuerst leisten; PV-Träger kann dann Regress nehmen
- Doppelbeantragung: immer sinnvoll; Träger klären intern ab

### Schritt 5 – Kombinationspflege
- Sachleistung (§ 36 SGB XI) + Geldleistung (§ 37 SGB XI): kombinierbar bei hälftigem Einsatz
- Bei Überlastung pflegender Angehöriger: Verhinderungspflege (§ 39 SGB XI) + Kurzzeitpflege

## Typische Fallen

- **Behandlungspflege vs. Grundpflege verwechselt**: Kasse lehnt ab weil Grundpflege; eigentlich Behandlungspflege (Insulingabe, Medikamentengabe durch Pflegedienst).
- **Hilfsmittelgutachten und Pflegegrad**: Pflegegrad-Gutachten beeinflusst Hilfsmittelbedarf; koordinieren.
- **Stationäre Pflege**: Im Pflegeheim übernimmt PV die Pflegekosten; GKV nur für Behandlung im Krankenhaus.
- **Rückforderung**: Wenn PV geleistet hat und GKV zuständig war → Erstattungsstreit (→ kv-057).

## Output-Formate

- Leistungsabgrenzungs-Matrix (individuell)
- Pflegehilfsmittelantrag (§ 40 SGB XI)
- Häusliche Krankenpflege-Antrag (§ 37 SGB V)
- Widerspruch gegen Pflegegrad-Ablehnung
- Koordinationsschreiben GKV ↔ PV

## Quellen

- [§ 14 SGB XI – Pflegebedürftigkeit](https://www.gesetze-im-internet.de/sgb_11/__14.html)
- [§ 40 SGB XI – Pflegehilfsmittel](https://www.gesetze-im-internet.de/sgb_11/__40.html)
- [§ 37 SGB V – Häusliche Krankenpflege](https://www.gesetze-im-internet.de/sgb_5/__37.html)
- [§ 13 SGB XI – Nachrang PV](https://www.gesetze-im-internet.de/sgb_11/__13.html)
- [BSG GKV/PV-Abgrenzung](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 37 SGB V](https://dejure.org/gesetze/SGB_V/37.html)

## 2. `kv-047-hospiz-palliativversorgung-und-sapv`

**Fokus:** GKV-Leistungen für sterbende Menschen: Hospizversorgung (§ 39a SGB V), SAPV (§ 37b SGB V), Zuzahlungsbefreiung und Versorgungskoordination.

# Hospiz, Palliativversorgung und SAPV

## Skill-Zweck

Sterbende Menschen und ihre Familien haben Anspruch auf umfassende palliative Versorgung. Dieser Skill klärt **GKV-Ansprüche im Bereich Hospiz, ambulante und stationäre Palliativversorgung und spezialisierte ambulante Palliativversorgung (SAPV)**.

## Rechtlicher Rahmen

- **§ 37b SGB V** – Spezialisierte ambulante Palliativversorgung (SAPV)
- **§ 39a SGB V** – Stationäre und ambulante Hospizleistungen
- **§ 39 SGB V** – Krankenhausbehandlung (Palliativstation)
- **§ 27 SGB V** – Krankenbehandlung: Anspruch umfasst Palliativmedizin
- **SAPV-Richtlinie des G-BA** (Stand 2023)
- BSG B 1 KR 2/22 R (SAPV-Anspruch), BSG B 1 KR 14/19 R

## Versorgungsformen im Überblick

| Versorgungsform | Rechtsgrundlage | Leistungsumfang | Zuzahlung |
|----------------|-----------------|-----------------|----------|
| Ambulante Palliativversorgung (APV) | § 27 SGB V, § 73 SGB V | Hausarzt + Palliativdienst | Normal |
| SAPV | § 37b SGB V | Spezialisiertes Team, 24h | Keine |
| Ambulante Hospizdienste | § 39a Abs. 2 SGB V | Ehrenamtliche + professionelle Begleitung | Keine |
| Stationäre Hospizversorgung | § 39a Abs. 1 SGB V | 95 % GKV-Finanzierung | 5 % Hospizbeitrag |
| Palliativstation (KH) | § 39 SGB V | Vollstationäre Behandlung | Normal (§ 39 Abs. 4) |

## Prüfprogramm

### Schritt 1 – SAPV-Anspruch (§ 37b SGB V)
- Voraussetzungen: nicht heilbare, weit fortgeschrittene Erkrankung mit begrenzter Lebenserwartung
- Besonderer Versorgungsbedarf: kann nicht durch Hausarzt alleine bewältigt werden
- Antrag: ärztliche Verordnung + Zustimmung Kasse (Genehmigungsfiktion § 13 Abs. 3a SGB V gilt)
- Team: spezialisiertes SAPV-Team (Arzt + Pflegekraft + ggf. Sozialarbeiter)

### Schritt 2 – Stationäre Hospizversorgung (§ 39a Abs. 1 SGB V)
- GKV übernimmt 95 % der Kosten; Hospiz-Eigenanteil ca. 5 %
- Voraussetzung: Sterben in absehbarer Zeit; Pflegegrad 3–5 oder mindestens 2 mit besonderem Pflegebedarf
- Zuzahlungsbefreiung: keine Zuzahlung in der Hospizversorgung
- Antrag bei Kasse mit Ärztlichem Attest und Hospiz-Aufnahmebescheid

### Schritt 3 – Ambulante Hospizdienste (§ 39a Abs. 2 SGB V)
- Palliative Care: 4 qualifizierte ehrenamtliche Stunden/Woche
- GKV fördert ambulante Hospizdienste; kostenlos für Versicherte
- Koordinierungsstellen in Kommunen; kein Antrag nötig

### Schritt 4 – Schmerztherapie und Palliativmedikation
- Opioide und Betäubungsmittel: ärztliche Verordnung nötig (BtMG)
- GKV-Leistung: Palliativmedikation vollständig erstattungsfähig
- Zuzahlung: grundsätzlich; Befreiung wenn Belastungsgrenze erreicht

### Schritt 5 – Koordination mit PV und Sozialleistungen
- Pflegeversicherung (SGB XI): ergänzende Leistungen; kein Ausschluss durch SAPV
- Sterbegeld: wurde abgeschafft; kein GKV-Anspruch mehr
- Hinterbliebenenberatung: Familien haben Anspruch auf psychosoziale Begleitung

## Typische Fallen

- **SAPV zu spät beantragt**: SAPV erst in allerletzter Phase beantragt; frühzeitige Verordnung ist sinnvoll wenn Kriterien erfüllt.
- **Hospiz-Eigenanteil**: Viele Familien wissen nicht dass sie 5 % selbst tragen; Sozialhilfe kann übernehmen (§ 74 SGB XII).
- **Genehmigungsfiktion**: Kasse reagiert nicht innerhalb 5 Wochen → SAPV gilt als genehmigt.
- **Krankenhausabrechnung Palliativstation**: Oft als DRG statt Palliativpauschale (OPS 8-98e) abgerechnet; bei langer Verweildauer prüfen.

## Output-Formate

- SAPV-Verordnungs-Checkliste (für Arzt)
- Hospiz-Aufnahmeantrag bei Kasse
- Zuzahlungsbefreiungs-Antrag
- Koordinationsbrief SAPV-Team + Hausarzt
- Hinterbliebenen-Informationsblatt

## Quellen

- [§ 37b SGB V – SAPV](https://www.gesetze-im-internet.de/sgb_5/__37b.html)
- [§ 39a SGB V – Hospiz](https://www.gesetze-im-internet.de/sgb_5/__39a.html)
- [SAPV-Richtlinie G-BA](https://www.g-ba.de/richtlinien/35/)
- [BSG B 1 KR 2/22 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [Deutsche Gesellschaft für Palliativmedizin](https://www.dgpalliativmedizin.de)
- [dejure.org § 37b SGB V](https://dejure.org/gesetze/SGB_V/37b.html)

## 3. `kv-048-krankenkassenregress-behandlungsfehler-und-erstattung`

**Fokus:** Regressansprüche der GKV gegen Leistungserbringer bei Behandlungsfehlern (§ 116 SGB X): Voraussetzungen, Höhe, Verjährung und Verhältnis zum Patientenanspruch.

# Krankenkassenregress: Behandlungsfehler und Erstattung

## Skill-Zweck

Wenn ein Behandlungsfehler Zusatzkosten für die GKV verursacht, kann die Kasse Regress nehmen. Dieser Skill klärt **Regressansprüche nach § 116 SGB X, Verhältnis zum Schadensersatzanspruch des Patienten und Koordinationspflichten**.

## Rechtlicher Rahmen

- **§ 116 SGB X** – Gesetzlicher Übergang von Schadensersatzansprüchen auf Sozialversicherungsträger
- **§ 119 SGB X** – Anspruchsübergang auf Kranken-/Pflegeversicherung
- **§ 83 SGB X** – Erstattungsansprüche zwischen Leistungsträgern
- **§ 630a ff. BGB** – Behandlungsvertrag; Schadensersatz bei Behandlungsfehlern
- **§ 291a SGB V** – Patientendaten-Schutz-Gesetz (Dokumentation)
- **PatRechteG 2013** – Patientenrechtegesetz (§ 630a–h BGB)
- BSG B 1 KR 26/07 R (Regressanspruch GKV), BGH VI ZR 91/17 (Schadensersatz und Regresskoordination)

## Regressstruktur § 116 SGB X

| Element | Inhalt |
|---------|--------|
| Schadensereignis | Behandlungsfehler, Unfall, Delikt durch Dritten |
| Schädiger | Arzt, Krankenhaus, sonstiger Dritter |
| Übergegangener Anspruch | Schadensersatz des Patienten geht auf GKV über (in Höhe der GKV-Leistungen) |
| Verjährung | 3 Jahre nach Kenntnis; absolute Grenze 30 Jahre (§ 199 BGB) |
| Koordination | GKV-Anspruch geht vor privatem Anspruch des Patienten auf gleichen Schadenposten |

## Prüfprogramm

### Schritt 1 – Regressvoraussetzungen
- Liegt ein Behandlungsfehler vor? (medizinischer Standard verletzt)
- Hat GKV Leistungen erbracht die kausal auf den Fehler zurückgehen?
- Schädiger identifiziert: Arzt, Krankenhaus, Haftpflichtversicherer?

### Schritt 2 – Anspruchsübergang (§ 116 SGB X)
- Übergang ist kraft Gesetzes automatisch (nicht konstitutiv)
- GKV-Leistungen: KH-Kosten, Medikamente, Reha, Krankengeld
- Umfang: GKV kann nur ihre eigenen Leistungen zurückfordern, nicht Schmerzensgeld

### Schritt 3 – Verhältnis zum Patienten
- Patient hat eigene Schadensersatzansprüche (Schmerzensgeld, Erwerbsausfall)
- GKV-Regress und Patientenanspruch können parallel bestehen; keine Doppelerstattung
- Informationspflicht: GKV muss Patienten über Regressanspruch informieren (indirekt)

### Schritt 4 – Patient fordert Schadensersatz
- Patient kann eigene Ansprüche neben GKV-Regress geltend machen
- Wichtig: Kein Vergleich über Ansprüche schließen ohne Zustimmung der GKV (soweit übergegangen)
- § 116 Abs. 1 Satz 2: Übergang gilt nicht soweit GKV-Mitglied keine wirtschaftlichen Nachteile hat

### Schritt 5 – MDK-Regress (§ 275 ff. SGB V)
- Andere Regressart: MDK prüft Krankenhausabrechnung; Kasse fordert zuviel gezahlte DRG zurück
- Kein Zusammenhang mit Behandlungsfehler-Regress

## Typische Fallen

- **Vergleich ohne GKV-Zustimmung**: Patient schließt Vergleich mit Arzt über alle Schäden; GKV-Anspruch trotzdem übergegangen → Vergleich bindet GKV nicht.
- **Verjährung Regress**: GKV muss Regress kennen; Verjährung beginnt mit Kenntnis, nicht mit Schadenseintritt.
- **Kausalität unklar**: Regressanspruch setzt gleiche Kausalitätsanforderungen wie Schadensersatzrecht (BGH VI ZR); schwieriger als im Sozialrecht.
- **Beweislast beim Arzt**: Bei groben Behandlungsfehlern Beweislastumkehr (§ 630h Abs. 5 BGB); hilft Patienten und damit indirekt der GKV.

## Output-Formate

- Regressanzeige an GKV (durch Patient)
- Koordinationsschreiben Patient ↔ GKV ↔ Haftpflichtversicherer
- Vergleichs-Checkliste (GKV-Beteiligung prüfen)
- Verjährungs-Fristenkalender
- MDK-Überprüfungsantrag (Behandlungsqualität)

## Quellen

- [§ 116 SGB X – Anspruchsübergang](https://www.gesetze-im-internet.de/sgb_10/__116.html)
- [§ 630a BGB – Behandlungsvertrag](https://www.gesetze-im-internet.de/bgb/__630a.html)
- [BSG B 1 KR 26/07 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [BGH VI ZR 91/17](https://www.bundesgerichtshof.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org § 116 SGB X](https://dejure.org/gesetze/SGB_X/116.html)
- [Bundesärztekammer Behandlungsfehler](https://www.bundesaerztekammer.de)
