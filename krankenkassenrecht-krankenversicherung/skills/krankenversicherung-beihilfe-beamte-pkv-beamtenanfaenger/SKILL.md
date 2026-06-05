---
name: krankenversicherung-beihilfe-beamte-pkv-beamtenanfaenger
description: "Beihilfe Beamte PKV Beamtenanfaenger: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Beihilfe Beamte PKV Beamtenanfaenger

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Beihilfe Beamte PKV Beamtenanfaenger** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-033-beihilfe-beamte-pkv-und-restkosten` | Beihilferecht für Beamte: Beihilfesatz, beihilfefähige Aufwendungen, PKV-Ergänzungsversicherung, Restkosten und Antragsfristen. |
| `kv-034-beamtenanfaenger-pauschale-beihilfe-laendercheck` | Öffnungsklausel für GKV bei Beamten, pauschale Beihilfe (Baden-Württemberg), Vergleich der Beihilfemodelle in den Bundesländern und GKV-Rückkehroption. |
| `kv-035-tarifwechsel-pkv-204-vvg` | Tarifwechselrecht in der PKV nach § 204 VVG: Voraussetzungen, Mitnahme der Altersrückstellungen, Risikoprüfung und Durchsetzung. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **Beihilfe Beamte PKV Beamtenanfaenger**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-033-beihilfe-beamte-pkv-und-restkosten`

**Fokus:** Beihilferecht für Beamte: Beihilfesatz, beihilfefähige Aufwendungen, PKV-Ergänzungsversicherung, Restkosten und Antragsfristen.

# Beihilfe, Beamte, PKV und Restkosten

## Skill-Zweck

Beamte finanzieren ihre Krankenversorgung aus zwei Quellen: **staatliche Beihilfe und private Krankenversicherung**. Dieser Skill klärt Beihilfesätze, beihilfefähige Aufwendungen und die Koordination mit der PKV.

## Rechtlicher Rahmen

- **§ 80 BBG** – Beihilfe für Bundesbeamte (Referenznorm)
- **Bundesbeihilfeverordnung (BBhV)** – Bundesbeamte: §§ 1–98 BBhV
- **Landesbeihilfeverordnungen** (je nach Land verschieden: BayBhV, BW-BVO etc.)
- **§ 193 VVG** – Restkostenversicherung PKV (Pflicht für Beamte)
- GOÄ, GOZ, GHD (Beihilfefähigkeit nach BBhV)
- BSG ist unzuständig; Verwaltungsgerichte (VG) entscheiden über Beihilfestreitigkeiten
- BVerwG Urt. v. 12.09.2018 – 5 C 7.17 (Beihilfe und medizinische Notwendigkeit)

## Beihilfesätze (Bundesbeamte, BBhV)

| Gruppe | Beihilfesatz |
|--------|-------------|
| Beamter selbst | 50 % |
| Mit ≥ 2 berücksichtigungsfähigen Kindern | 70 % |
| Ehegatten/eingetragene Lebenspartner | 70 % |
| Kinder | 80 % |
| Versorgungsempfänger (Pensionäre) | 70 % |

## Prüfprogramm

### Schritt 1 – Beihilfefähigkeit der Aufwendung
- Ist die Leistung im Katalog der beihilfefähigen Aufwendungen (§§ 18–42 BBhV)?
- Ärztliche Behandlung: GOÄ-Abrechnung, Steigerungsfaktoren prüfen (Beihilfe nur bis Faktorgrenzen)
- Zahnarztkosten: GOZ, auch hier Steigerungsfaktoren begrenzt
- Arzneimittel: Nur wenn mit ärztlicher Verordnung und zugelassen; Lifestyle-Ausschluss

### Schritt 2 – PKV-Restkostenversicherung
- Beihilfe deckt 50/70/80 %; PKV deckt Restbetrag
- PKV muss so abgestimmt sein dass keine Überschneidung entsteht
- Wichtig: PKV-Tarif als Ergänzungsversicherung, nicht als Vollversicherung bei Beamten

### Schritt 3 – Beihilfeantrag
- Antrag binnen 1 Jahr nach Aufwendung (Ausschlussfrist, je nach Land variiert)
- Belege: Originalrechnungen, Rezepte, Arztberichte
- Dienstherr (Bundeskasse, Landesamt etc.) bearbeitet Antrag

### Schritt 4 – Ablehnung und Widerspruch
- Verwaltungsgerichtsweg: Widerspruch gegen Beihilfebescheid
- Dann Klage beim Verwaltungsgericht (nicht Sozialgericht!)
- Typische Ablehnungsgründe: fehlende medizinische Notwendigkeit, nicht beihilfefähige Methode, überhöhte GOÄ-Abrechnung

### Schritt 5 – Landesvariationen
- Bayern: BayBhV abweichend von BBhV; Steigerungsfaktoren oft strenger
- Baden-Württemberg: Pauschale Beihilfe für Anfänger (→ kv-034)
- Berlin: Öffnungsklausel GKV möglich; beachte Wechseloptionen

## Typische Fallen

- **Ausschlussfrist**: 1-Jahres-Frist (manche Länder 2 Jahre) für Antragstellung; verpasste Frist = kein Anspruch.
- **Rechnungsfehler GOÄ**: Arzt rechnet falsch ab → PKV kürzt → Differenz zu Lasten des Beamten.
- **Außenseitermethoden**: Homöopathie, Anthroposophie – beihilfefähig nach BBhV § 18; aber landesspezifisch unterschiedlich.
- **Belegärzte**: Kosten belegärztlicher Behandlung werden oft unterschätzt; PKV-Tarif prüfen.

## Output-Formate

- Beihilfeantrag (Muster, Bund)
- Widerspruch gegen Beihilfe-Ablehnung
- PKV-Ergänzungsversicherungs-Checkliste
- GOÄ-Abrechnungsprüfung
- Verwaltungsgerichtsklage (kurze Übersicht)

## Quellen

- [Bundesbeihilfeverordnung BBhV](https://www.gesetze-im-internet.de/bbhv/)
- [§ 80 BBG – Beihilfe](https://www.gesetze-im-internet.de/bbg_2009/__80.html)
- [§ 193 VVG – Versicherungspflicht](https://www.gesetze-im-internet.de/vvg_2008/__193.html)
- [BVerwG Beihilfe-Entscheidungen](https://www.bverwg.de/entscheidungen)
- [PKV-Verband Beamte](https://www.pkv.de/wissen/beihilfe/)
- [dejure.org BBhV](https://dejure.org/gesetze/BBhV)

## 2. `kv-034-beamtenanfaenger-pauschale-beihilfe-laendercheck`

**Fokus:** Öffnungsklausel für GKV bei Beamten, pauschale Beihilfe (Baden-Württemberg), Vergleich der Beihilfemodelle in den Bundesländern und GKV-Rückkehroption.

# Beamtenanfänger: Pauschale Beihilfe, Ländercheck

## Skill-Zweck

Beamtenanfänger müssen die PKV vs. GKV-Entscheidung treffen. Einige Bundesländer bieten **pauschale Beihilfe** an (GKV-Wahlrecht). Dieser Skill vergleicht die Ländermodelle und zeigt Vor- und Nachteile auf.

## Rechtlicher Rahmen

- **§ 80 BBG** – Bundesbeamte: klassische Beihilfe
- **Länderbeamtengesetze** – variieren je Land erheblich
- **§ 193 Abs. 3 VVG** – Beamte müssen versichert sein
- **§ 6 Abs. 1 Nr. 2 SGB V** – Beamte als versicherungsfrei
- **BW-Beamtengesetz §§ 78c ff.** – Pauschale Beihilfe Baden-Württemberg
- **BayBhV** – Bayerische Beihilfeverordnung (kein Pauschalmodell)
- Verschiedene Urteile der Verwaltungsgerichte der Länder

## Ländervergleich Beihilfemodelle

| Land | Pauschalbeihilfe | GKV möglich | Besonderheiten |
|------|-----------------|------------|----------------|
| Baden-Württemberg | Ja (§ 78c BW LBG) | Ja, für neue Beamte | Monatlicher Zuschuss statt prozentuale Erstattung |
| Bayern | Nein | Nein | Strikte Beihilfe + PKV |
| Berlin | Öffnungsklausel | Ja, bedingt | Auf Antrag möglich |
| Hamburg | Beihilfe modernisiert | Eingeschränkt | Eigene Landesbeihilfeverordnung |
| Bund | Nein | Nein | BBhV + PKV obligatorisch |

## Prüfprogramm

### Schritt 1 – Welches Land, welches Dienstrecht?
- Bundesbeamter: BBhV + PKV obligatorisch
- Landesbeamter: Landesbeihilferecht prüfen
- Welches Bundesland? Dienstbeginn-Datum relevant (manche Regeln nur für Neueintretende)

### Schritt 2 – Baden-Württemberg: Pauschale Beihilfe
- Für Beamte mit Dienstbeginn nach 01.01.2013 möglich
- Zuschuss: Monatlicher Festbetrag (pauschal), unabhängig von tatsächlichen Ausgaben
- GKV-Wahl: Beamter zahlt GKV-Beitrag minus pauschalem Zuschuss
- Vorteil: Familienversicherung möglich (Kinder beitragsfrei)
- Nachteil: Keine individuelle Erstattung; hohe Gesundheitskosten werden nicht voll abgedeckt

### Schritt 3 – Kostenvergleich PKV vs. GKV (Pauschalbeihilfe)
- PKV: niedrige Beiträge bei Berufsstart + Beihilfe 50 %; aber: steigende Beiträge im Alter
- GKV (Pauschalbeihilfe): einkommensabhängige Beiträge; Familienversicherung günstig
- Langzeitperspektive: PKV günstiger für Single ohne Kinder; GKV günstiger für Familien

### Schritt 4 – Rückkehr in GKV
- Beamter wählt PKV → Rückkehr in GKV nur bei Unterschreiten JAEG (durch Nebentätigkeit) oder Statuswechsel (Entlassung aus Beamtenverhältnis)
- Entscheidung ist langfristig; Beratung vor Dienstantritt wichtig

### Schritt 5 – Beamtenanfänger-Checkliste
- Dienstrecht klären (Bund, welches Land?)
- Pauschale Beihilfe Option? (nur BW, Berlin teilweise)
- PKV-Angebote vergleichen (ohne Risikoprüfung bei Berufsstart)
- Langfristprojektion: Beitragsanstieg im Alter berücksichtigen

## Typische Fallen

- **PKV-Beitragsanstieg vergessen**: Im Alter steigen PKV-Beiträge erheblich; Altersrückstellungen prüfen.
- **Familienplanung und PKV**: Jedes Kind muss separat versichert werden; GKV-Familienversicherung wäre beitragsfrei.
- **Probezeit-Status**: In Probezeit gilt oft kein voller Beihilfesatz; verringerte Beihilfe in ersten Jahren.
- **Dienstherr wechselt Bundesland**: Beihilferecht wechselt mit; PKV bleibt gleich.

## Output-Formate

- Beihilfe vs. GKV-Vergleichsrechnung
- Länder-Beihilfeverordnungs-Übersicht
- Entscheidungshilfe Beamtenanfänger (Flussdiagramm)
- PKV-Antragsprüfung (ohne Risikoprüfung-Frist nutzen)
- Pauschale-Beihilfe-Antrag BW (Muster)

## Quellen

- [Bundesbeihilfeverordnung BBhV](https://www.gesetze-im-internet.de/bbhv/)
- [BW Landesbeamtengesetz § 78c](https://landesrecht.bw.de)
- [§ 6 SGB V – Versicherungsfreiheit Beamte](https://www.gesetze-im-internet.de/sgb_5/__6.html)
- [PKV-Verband Beamtenversorgung](https://www.pkv.de/wissen/beihilfe/)
- [dejure.org § 6 SGB V](https://dejure.org/gesetze/SGB_V/6.html)
- [Verwaltungsgericht Stuttgart Beihilfe](https://www.vgh-bw.de)

## 3. `kv-035-tarifwechsel-pkv-204-vvg`

**Fokus:** Tarifwechselrecht in der PKV nach § 204 VVG: Voraussetzungen, Mitnahme der Altersrückstellungen, Risikoprüfung und Durchsetzung.

# Tarifwechsel PKV: § 204 VVG

## Skill-Zweck

Wer in der PKV zu einem günstigeren oder leistungsfähigeren Tarif beim gleichen Versicherer wechseln will, hat ein gesetzliches Recht dazu. Dieser Skill klärt **§ 204 VVG: Voraussetzungen, Altersrückstellungen und Durchsetzungsstrategien**.

## Rechtlicher Rahmen

- **§ 204 VVG** – Tarifwechselrecht: gleicher Versicherer, gleichartiger Tarif, Mitnahme Altersrückstellungen
- **§ 146 Abs. 1 VAG** – Kalkulationsvorschriften (Altersrückstellungen)
- **MB/KK 2009 § 13** – Tarifwechsel-Klausel in den Bedingungen
- BGH IV ZR 118/11 (§ 204 VVG, Altersrückstellungen), BGH IV ZR 307/20 (Tarifwechsel und neue Risikoprüfung)
- OLG München 25 U 5677/18 (Ablehnung Tarifwechsel, Begründungspflicht)

## § 204 VVG – Kerngehalt

| Recht | Inhalt |
|-------|--------|
| Wechselrecht | Anspruch auf Wechsel in anderen Tarif beim gleichen Versicherer |
| Altersrückstellungen | Anteilige Mitnahme in neuen Tarif |
| Risikoprüfung | Grundsätzlich nicht zulässig für Altrückstellungs-Anteil |
| Mehrleistungen | Für Mehrleistungen des neuen Tarifs: Risikoprüfung erlaubt |
| Wartezeiten | Für bisher versicherte Leistungen keine neue Wartezeit |

## Prüfprogramm

### Schritt 1 – Tarif-Vergleich
- Welcher Tarif ist das Ziel? Gleichartiger Tarif nach § 204 VVG: ähnliche Leistungsstruktur
- Ist der Zieltarif noch für Neukunden offen? (manche Tarife geschlossen)
- Leistungsunterschiede: Mehrleistungen können Risikoprüfung auslösen

### Schritt 2 – Altersrückstellungen berechnen
- PKV-Versicherer führen für jeden Versicherten Altersrückstellungen
- Bei Tarifwechsel innerhalb des Versicherers: volle Mitnahme der angesammelten Rückstellungen
- Mathematisch: Rückstellungen erhöhen den Wechselwert; Versicherer muss transparente Berechnung liefern

### Schritt 3 – Risikoprüfung bei Mehrleistungen
- Zieltarif bietet Mehrleistungen (z.B. Chefarztbehandlung im Ausland): für diesen Teil neue Risikoprüfung möglich
- PKV darf Leistungsausschluss setzen oder Risikozuschlag für Mehrleistungsanteil verlangen
- Für gleiche Leistungen wie bisher: keine neue Risikoprüfung

### Schritt 4 – Antragstellung und PKV-Verhalten
- Schriftlicher Antrag beim Versicherer
- PKV hat keine bestimmte Antwortfrist; aber unverzüglich (AGB-Kontrolle)
- Ablehnung: BGH → PKV muss Ablehnung begründen; bloßes „nicht möglich" reicht nicht
- Klage: Zivilgericht; Anspruch auf Tarifwechsel durchsetzen

### Schritt 5 – Wechsel zum anderen Versicherer
- § 204 VVG gilt nur innerhalb desselben Versicherers
- Wechsel zu neuem Versicherer: neue Risikoprüfung, keine Rückstellungsmitnahme
- Ausnahme: Basistarif-Wechsel ohne Risikoprüfung (§ 152 VAG)

## Typische Fallen

- **Geschlossener Tarif**: Versicherer behauptet Tarif ist geschlossen; Rechtsprechung: Bestandsversicherte haben trotzdem Wechselrecht.
- **Transparenz der Rückstellungen**: Versicherer weist Rückstellungen nicht aus; Auskunftsrecht (§ 305 VVG analog).
- **Kombination mit Beitragsanpassung**: Nach BA-Erhöhung ist § 204-Wechsel besonders interessant (günstigerer Tarif ohne Beitragserhöhung).
- **Ehegatten-Mitversicherung**: Mitversicherte Ehegatten haben eigenes Wechselrecht; separat prüfen.

## Output-Formate

- Tarifwechsel-Antrag (§ 204 VVG, Muster)
- Altersrückstellungs-Auskunftsverlangen
- Ablehnung-Widerspruch (Begründungspflicht)
- Zivilklageschrift Tarifwechsel
- Tarif-Vergleichsmatrix

## Quellen

- [§ 204 VVG – Tarifwechsel](https://www.gesetze-im-internet.de/vvg_2008/__204.html)
- [BGH IV ZR 118/11](https://www.bundesgerichtshof.de/DE/Entscheidungen/entscheidungen_node.html)
- [BGH IV ZR 307/20](https://www.bundesgerichtshof.de/DE/Entscheidungen/entscheidungen_node.html)
- [§ 146 VAG – Altersrückstellungen](https://www.gesetze-im-internet.de/vag_2016/__146.html)
- [dejure.org § 204 VVG](https://dejure.org/gesetze/VVG/204.html)
- [PKV-Verband Tarifwechsel](https://www.pkv.de)
