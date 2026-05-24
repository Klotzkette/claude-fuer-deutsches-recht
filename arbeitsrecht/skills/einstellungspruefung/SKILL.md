---
name: einstellungspruefung
description: "Prüfung von Arbeitsvertrag und Befristung bei Neueinstellungen – TzBfG (Sachgrund, Vorbeschäftigungsverbot), AGG (diskriminierungsfreie Ausschreibung und Einstellung), AÜG (Abgrenzung Arbeitnehmerüberlassung), Nachweisgesetz sowie nachvertragliche Wettbewerbsverbote (§§ 74 ff. HGB)."
---

# /arbeitsrecht:einstellungsprüfung

## Zweck

Standardarbeitsverträge sind meistens unproblematisch – bis sie es nicht mehr sind. Die Befristungsklausel, die nach 24 Monaten zur unbefristeten Beschäftigung führt, weil das Vorbeschäftigungsverbot nicht geprüft wurde. Die Wettbewerbsklausel, die mangels Karenzentschädigung nichtig ist. Die Stellenausschreibung, die AGG-widrig formuliert ist. Dieser Skill findet diese Probleme, bevor sie entstehen.

## Eingaben

- Arbeitsvertragsentwurf (oder Beschreibung des geplanten Arbeitsverhältnisses)
- Art der Befristung (sachgrundlos nach § 14 Abs. 2 TzBfG oder mit Sachgrund nach § 14 Abs. 1 TzBfG)
- Vorherige Beschäftigungen beim selben Arbeitgeber (für Vorbeschäftigungsverbot)
- Position, Vergütung, Arbeitsort
- Ggf. Stellenausschreibungstext
- `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` → Einstellungsregeln, Standort

## Ablauf

### 1. Kontext laden

Konfiguration lesen: Einstellungsregeln, Standardmuster, Wettbewerbsklauselrichtlinie, Standort-Fußabdruck. Falls Mandantenakten aktiviert: Aktiven Kontext laden.

### 2. Befristungsprüfung (§§ 14–17 TzBfG)

**Sachgrundlose Befristung (§ 14 Abs. 2 TzBfG):**
- Höchstdauer: 2 Jahre, maximal 3-malige Verlängerung innerhalb dieser 2 Jahre
- **Vorbeschäftigungsverbot (§ 14 Abs. 2 S. 2 TzBfG):** Sachgrundlose Befristung unzulässig, wenn der Arbeitnehmer bereits zuvor beim selben Arbeitgeber beschäftigt war – auch bei länger zurückliegenden Beschäftigungen (BAG, Urt. v. 23.01.2019 – 7 AZR 733/16, NZA 2019, 1042: kein zeitliches Limit des Vorbeschäftigungsverbots im Regelfall `[Modellwissen – prüfen]`; anders noch BAG, Urt. v. 06.04.2011 – 7 AZR 716/09, NZA 2011, 905: 3-Jahres-Grenze; durch BVerfG, Beschl. v. 06.06.2018 – 1 BvL 7/14, NJW 2018, 2542 für Grundgesetz-konform erklärt, wenn Gerichte pragmatisch auslegen `[Modellwissen – prüfen]`)
- Klausel prüfen: „Die Befristung erfolgt gem. § 14 Abs. 2 TzBfG" – exakte Benennung des Befristungsgrunds erforderlich (BAG, Urt. v. 10.10.2007 – 7 AZR 795/06, NZA 2008, 245 Rn. 17 `[Modellwissen – prüfen]`)
- 3-Wochen-Klagefrist nach § 17 TzBfG beachten (analog § 4 KSchG)

**Sachgrundbefristung (§ 14 Abs. 1 TzBfG):**
Sachgründe prüfen:
1. Vorübergehender Bedarf (Nr. 1) – konkrete Prognose erforderlich (ErfK/Müller-Glöge, 24. Aufl. 2024, § 14 TzBfG Rn. 30 ff. `[Modellwissen – prüfen]`)
2. Im Anschluss an Ausbildung/Studium (Nr. 2)
3. Zur Vertretung eines anderen Arbeitnehmers (Nr. 3) – indirekter Vertretungsbedarf ausreichend (BAG, Urt. v. 25.03.2009 – 7 AZR 34/08, NZA 2009, 1155 `[Modellwissen – prüfen]`)
4. Eigenart der Arbeitsleistung (Nr. 4)
5. Zur Erprobung (Nr. 5) – max. 6 Monate (BAG, Urt. v. 02.06.2010 – 7 AZR 136/09, NZA 2010, 1248 `[Modellwissen – prüfen]`)
6. In der Person des Arbeitnehmers liegende Gründe (Nr. 6)
7. Haushaltsmittelfinanzierung im öffentlichen Dienst (Nr. 7)
8. Gerichtlicher Vergleich (Nr. 8)

**Befristungsabrede schriftlich?** § 14 Abs. 4 TzBfG: Schriftformerfordernis (§ 126 BGB). Elektronische Form (§ 126a BGB) **nicht** ausreichend (BAG, Urt. v. 16.04.2008 – 7 AZR 1048/06, NZA 2008, 999 `[Modellwissen – prüfen]`). Unterschrift vor Arbeitsaufnahme!

### 3. AGG-Prüfung (§§ 1–7 AGG)

- Stellenausschreibung diskriminierungsfrei? § 11 AGG: keine Merkmale nach § 1 AGG (Rasse, Geschlecht, Religion, Weltanschauung, Behinderung, Alter, sexuelle Identität)
- Auswahlverfahren dokumentiert? § 22 AGG: Indizienbeweislast beim Arbeitgeber, wenn Diskriminierungsmerkmale kausal erscheinen
- Altersgrenzen in Ausschreibung? § 10 AGG: Rechtfertigung nur bei sachlichem Grund (z.B. tarifliche Altersgrenze; BAG, Urt. v. 21.09.2017 – 2 AZR 57/17, NZA 2018, 226 Rn. 38 `[Modellwissen – prüfen]`)
- Entschädigungsanspruch bei unterlassenem Einladungsnachweis: § 15 Abs. 2 AGG bis zu 3 Monatsverdienste

### 4. Nachweispflichten (NachwG)

Seit 01.08.2022 (Reform durch Gesetz v. 20.07.2022, BGBl. I S. 1174): Erstnachweis am ersten Arbeitstag schriftlich (keine elektronische Form), spätestens am 7. Arbeitstag für Kernbedingungen:
- Name und Anschrift der Parteien
- Beginn und ggf. Ende des Arbeitsverhältnisses
- Arbeitsort (alle Einsatzorte bei wechselnden)
- Tätigkeit / Berufsbezeichnung
- Vergütung (Grundvergütung, Zuschläge, Fälligkeit)
- Vereinbarte Arbeitszeit (auch Überstundenregelung)
- Urlaub
- Kündigungsfristen
- Verfahren bei Kündigung
- **Neu seit 2022:** Hinweis auf anwendbaren Tarifvertrag/Betriebsvereinbarung; Probezeit; Fälligkeit der Vergütung; Zusammensetzung der Vergütung

Bußgeld nach § 4 NachwG bei Verletzung: bis 2.000 € je Arbeitnehmer.

### 5. AGB-Kontrolle (§§ 305–310 BGB)

Arbeitsverträge unterliegen der AGB-Kontrolle, wenn Arbeitgeber Vorformulierungen verwendet (BAG, Urt. v. 19.01.2011 – 10 AZR 738/09, NZA 2011, 631 Rn. 25 `[Modellwissen – prüfen]`):
- Freiwilligkeitsvorbehalt bei variablen Vergütungsbestandteilen: Wirksam nur wenn klar formuliert, kein Widerspruch zu anderen Klauseln (Grüneberg, 83. Aufl. 2024, § 305c BGB Rn. 10 ff. `[Modellwissen – prüfen]`)
- Rückzahlungsklauseln (Ausbildungskosten, Umzugskosten): Bindungsdauer proportional zur Leistungshöhe; BAG, Urt. v. 06.09.2017 – 10 AZR 558/16, NZA 2018, 46 `[Modellwissen – prüfen]`
- Nachvertragliche Wettbewerbsverbote §§ 74 ff. HGB: **Karenzentschädigung ≥ 50 % des zuletzt bezogenen Entgelts** (§ 74 Abs. 2 HGB) zwingend. Fehlt sie: Verbot unverbindlich (§ 74a Abs. 1 HGB) – Arbeitnehmer kann wählen; Arbeitgeber kann nicht klagen.

### 6. AÜG-Abgrenzung (§§ 1, 12 AÜG)

Falls Einsatz von Leiharbeitnehmern oder Werk-/Dienstverträgen geplant:
- Höchstüberlassungsdauer § 1 Abs. 1b AÜG: 18 Monate (verlängerbar durch TV/BV)
- Equal Pay nach § 8 AÜG ab Monat 10; durch TV abweichbar (HWK/Krause, 10. Aufl. 2022, § 8 AÜG Rn. 5 ff. `[Modellwissen – prüfen]`)
- Scheinselbständigkeit bei Werkvertrag? § 611a BGB-Kriterien anlegen

### 7. Betriebsrat (§ 99 BetrVG)

Falls Betriebsrat vorhanden: § 99 BetrVG – Zustimmung vor jeder Einstellung (in Betrieben mit > 20 wahlberechtigten AN). Unterlassener Antrag: keine Wirksamkeitssanktion für Arbeitsvertrag, aber Ordnungswidrigkeit und ggf. Unterlassungsklage nach § 23 Abs. 3 BetrVG.

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-buergerliches-recht.md`.

Wesentliche Quellen:
- Müller-Glöge (begr.) / Preis / Schmidt, in: ErfK, 25. Aufl. 2025, § 14 TzBfG (Befristungsrecht umfassend; Müller-Glöge verstorben 2018, Werk wird fortgeführt unter den Hrsg. Preis/Sittard/Kiel)
- Roloff, in: BeckOK ArbR, 71. Ed. 2025, § 14 TzBfG Rn. 1 ff.
- BAG, Urt. v. 23.01.2019 – 7 AZR 733/16, NZA 2019, 1042 (Vorbeschäftigungsverbot)
- BVerfG, Beschl. v. 06.06.2018 – 1 BvL 7/14, NJW 2018, 2542 (Verfassungskonformität § 14 Abs. 2 TzBfG)
- BAG, Urt. v. 16.04.2008 – 7 AZR 1048/06, NZA 2008, 999 (Schriftform Befristungsabrede)
- Thüsing, in: MüKoBGB, 9. Aufl. 2022, § 611a BGB Rn. 80 ff. (Arbeitnehmerbegriff, AÜG-Abgrenzung)

## Ausgabeformat

Strukturierte Einstellungsprüfung als Memo:

```
EINSTELLUNGSPRÜFUNG – [Position] – [Datum]
VERTRAULICH – MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO

Ergebnis: [🟢 Freigabe / 🟡 Freigabe mit Auflagen / 🔴 Nicht freigegeben]

⚠️ Prüfhinweis: [Quellen, Leseumfang, Flags, Aktualität]

I.   Befristungsprüfung  [🟢 / 🟡 / 🔴]
     Befristungsart: [§ 14 I oder II TzBfG]
     Sachgrund: [Bezeichnung] – [Subsumtion]
     Vorbeschäftigung: [Ergebnis]
     Schriftform: [ja/nein]

II.  AGG-Prüfung        [🟢 / 🟡 / 🔴]
     Ausschreibung: [OK / Flag]
     Auswahlverfahren: [OK / Flag]

III. NachwG             [🟢 / 🟡]
     Fehlende Pflichtangaben: [Liste]

IV.  AGB-Kontrolle      [🟢 / 🟡 / 🔴]
     Flags: [Klausel, Risiko, Empfehlung]

V.   AÜG (falls relevant) [🟢 / 🟡 / 🔴]

VI.  Betriebsrat        [ggf. § 99 BetrVG]

Handlungsempfehlungen:
  1. ...
  2. ...

Wie weiter? [Entscheidungsbaum]
```

## Beispiele

**Beispiel – Sachgrundlose Befristung mit Vorbeschäftigung:**

*Sachverhalt:* Frau M. soll auf 18 Monate sachgrundlos nach § 14 Abs. 2 TzBfG befristet als Projektmanagerin eingestellt werden. Sie war vor 3 Jahren für 6 Monate beim selben Arbeitgeber als Werkstudentin tätig.

*Prüfung (Gutachtenstil):*

**Obersatz:** Die sachgrundlose Befristung ist gem. § 14 Abs. 2 S. 2 TzBfG unzulässig, wenn Frau M. zuvor beim Arbeitgeber beschäftigt war.

**Definition:** § 14 Abs. 2 S. 2 TzBfG verbietet die sachgrundlose Befristung, wenn zwischen denselben Parteien bereits zuvor ein Arbeitsverhältnis bestand. Das BAG hat in seiner Grundsatzentscheidung v. 23.01.2019 (7 AZR 733/16, NZA 2019, 1042 Rn. 21) die frühere 3-Jahres-Grenze aufgegeben und betont, das Verbot gelte zeitlich unbegrenzt, sofern kein Ausnahmetatbestand greife `[Modellwissen – prüfen]`. Das BVerfG (Beschl. v. 06.06.2018 – 1 BvL 7/14, NJW 2018, 2542) hat klargestellt, dass ein sehr weit zurückliegendes Erstarbeitsverhältnis als Ausnahme behandelt werden kann, wenn es unzumutbar wäre, darauf abzustellen.

**Subsumtion:** Frau M. war vor 3 Jahren als Werkstudentin tätig. Das Werkstudentenverhältnis ist ein Arbeitsverhältnis i.S.d. § 611a BGB. Die 3-jährige Unterbrechung ist nach BAG-Rspr. nicht ausreichend, um das Vorbeschäftigungsverbot zu überwinden; es sei denn, das Erstarbeitsverhältnis war ganz anders geartet und sehr kurz. 6 Monate Werkstudentenbeschäftigung 3 Jahre zurückliegend: Grenzfall `[prüfen]`.

**Ergebnis:** 🔴 Sachgrundlose Befristung mit erheblichem Risiko. Empfehlung: Sachgrundsbefristung (§ 14 Abs. 1 Nr. 5 TzBfG – Erprobung) oder unbefristetes Arbeitsverhältnis erwägen. Außenanwalt einbeziehen.

## Risiken / typische Fehler

- **Vorbeschäftigungsverbot** – häufigster Fehler: auch kurze, lange zurückliegende, andersartige Vorbeschäftigungen aktivieren § 14 Abs. 2 S. 2 TzBfG.
- **Schriftform der Befristungsabrede** – muss VOR Arbeitsaufnahme unterschrieben sein; digitale Unterschrift genügt nicht (§ 14 Abs. 4 TzBfG, § 126 BGB).
- **3-Wochen-Klagefrist** § 17 TzBfG – läuft ab Ende des befristeten Arbeitsverhältnisses; Versäumung führt zu Fiktion der Wirksamkeit der Befristung.
- **NachwG-Reform 2022** – neu eingeführte Pflichtangaben sind vielen Arbeitgebern unbekannt; Bußgeld bis 2.000 € je Verstoß.
- **Wettbewerbsverbot ohne Karenzentschädigung** – führt zu Unverbindlichkeit (§ 74a HGB), nicht zur Nichtigkeit; Arbeitnehmer kann das Verbot trotzdem gegen sich gelten lassen.
