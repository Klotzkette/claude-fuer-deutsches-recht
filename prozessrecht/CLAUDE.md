# Prozessrecht-Plugin – Praxiskonfiguration

> Diese Datei wird vom Cold-Start-Interview geschrieben und angepasst. Sie enthält das Praxisprofil der Kanzlei bzw. Rechtsabteilung und steuert alle Skills. Vor dem ersten Einsatz das Cold-Start-Interview mit `/cold-start` ausführen.

---

## 1. Rechtsrahmen und Verfahrensordnungen

Dieses Plugin arbeitet ausschließlich nach **deutschem Recht**. Maßgebliche Verfahrensordnungen:

| Verfahren | Primäres Regelwerk | Ergänzende Regelwerke |
|---|---|---|
| Zivilprozess | ZPO | GVG, GKG, RVG, EGZPO |
| Strafprozess | StPO | GVG, StGB, RVG, JGG |
| Verwaltungsstreit | VwGO | VwVfG (Bund/Länder), GKG |
| Finanzgerichtsbarkeit | FGO | AO, UStG, GKG |
| Sozialgerichtsbarkeit | SGG | SGB I–XII, GKG |
| Arbeitsgerichtsbarkeit | ArbGG | KSchG, BetrVG, BGB, RVG |
| Familiensachen / FGG | FamFG | BGB, GKG |
| Zwangsvollstreckung | §§ 704–915h ZPO | ZVG, InsO, RPflG |

---

## 2. Vorprozessuale Beweiserhebung im deutschen Recht

Das deutsche Zivilprozessrecht beruht auf dem Beibringungsgrundsatz (§§ 282, 283 ZPO). Vorprozessuale Beweiserhebung ist auf eng begrenzte gesetzliche Instrumente beschränkt. Jeder Skill, jede Ausgabe und jedes Memo muss dies berücksichtigen.

### Informationsbeschaffung im deutschen Recht – Übersicht

| Instrument | Rechtsgrundlage | Inhalt |
|---|---|---|
| Gerichtliche Urkundenvorlegung | §§ 142, 143 ZPO | Gericht kann Vorlage von Urkunden anordnen (kein Parteienrecht!) |
| Augenschein | § 144 ZPO | Sachverständige, Besichtigung durch Gericht |
| Einsichtnahme in Urkunden | § 810 BGB | Anspruch auf Einsicht bei rechtlichem Interesse |
| Auskunftsansprüche (allgemein) | §§ 242, 259, 260, 666 BGB | Treu und Glauben; Rechenschaftspflicht; Auftragsrecht |
| Datenschutz-Auskunft | Art. 15 DSGVO | Auskunft über gespeicherte personenbezogene Daten |
| Stufenklage | § 254 ZPO | Auskunft, Abgabe einer eidesstattlichen Versicherung, Leistung |
| Selbständiges Beweisverfahren | §§ 485 ff. ZPO | Sicherung von Beweismitteln vor oder nach Klageerhebung |
| Aktenvorlage im Strafverfahren | §§ 161a, 163a StPO | Zeugen- und Sachverständigenladung durch StA |
| Urkundenvorlage Dritter | §§ 421–431 ZPO | Aufforderung und ggf. gerichtliche Anordnung |
| IFG/UIG/VIG | IFG, UIG, VIG | Informationsfreiheitsansprüche gegen Behörden |

**Hinweis für Schriftsätze:** Immer die konkrete deutsche Norm nennen.

---

## 3. Mandatsgeheimnis und Berufsrecht

Alle Ausgaben stehen unter dem Vorbehalt der anwaltlichen Verschwiegenheit:

- **§ 43a Abs. 2 BRAO** – Kernpflicht der Verschwiegenheit
- **§ 203 Abs. 1 Nr. 3 StGB** – Strafbewehrtes Berufsgeheimnis
- **§ 53 Abs. 1 Nr. 3 StPO** – Zeugnisverweigerungsrecht des Anwalts
- **§ 383 Abs. 1 Nr. 6 ZPO** – Zeugnisverweigerungsrecht im Zivilverfahren
- **§ 97 StPO** – Beschlagnahmefreiheit anwaltlicher Kommunikation
- **§ 160a StPO** – Kernbereichsschutz bei Überwachungsmaßnahmen

**Mandatsgeheimnismarker:** Alle generierten Dokumente tragen den Vermerk `MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO / § 203 StGB`. Dateien für die Übermittlung an Dritte werden separat markiert.

---

## 4. Zitierweise

Verbindlich: `../references/zitierweise.md`.

**Kurzreferenz:**
- Rechtsprechung: `BGH, Urt. v. 13.07.2022 – VIII ZR 317/21, NJW 2022, 2754 Rn. 21.`
- Kommentar: `Greger, in: Zöller, ZPO, 35. Aufl. 2024, § 286 Rn. 14.`
- Aufsatz: `Grigoleit, NJW 2020, 1873 (1876).`

Für das Prozessrecht maßgebliche Kommentarwerke:
- **Zöller** – Zöller, ZPO (35. Aufl. 2024)
- **Musielak/Voit** – Musielak/Voit, ZPO (aktuellste Aufl.)
- **Stein/Jonas** – Stein/Jonas, ZPO (23. Aufl. 2024)
- **MüKoZPO** – Münchener Kommentar zur ZPO (6. Aufl. 2020)
- **BeckOK ZPO** – BeckOK ZPO (aktuelle Edition)
- **Karlsruher Kommentar StPO** – KK-StPO (9. Aufl. 2023)
- **Meyer-Goßner/Schmitt** – StPO (67. Aufl. 2024)
- **MüKoStPO** – Münchener Kommentar zur StPO (2. Aufl. 2024)

---

## 5. Methodik

- **Gutachtenstil** als Standard für interne Memos und Analysen.
- **Urteilsstil** für Schriftsätze, Briefe, Protokolle.
- **h.M./Gegenauffassung** immer mit Belegen; keine Floskeln ohne Fundstelle.
- **Keine Präjudizienbindung**: Urteile sind argumentativ überzeugend, aber nicht bindend (Ausnahme: § 31 BVerfGG für BVerfG-Entscheidungen nach § 31 Abs. 2 BVerfGG).
- **Kommentarliteratur** ist tragende Argumentationsquelle, besonders bei fehlendem oder uneindeutigem höchstrichterlichem Urteil.

---

## 6. Praxisprofil (wird durch Cold-Start befüllt)

```yaml
kanzlei_typ: ""             # z. B. "Einzelanwalt", "Sozietät", "Rechtsabteilung"
praxis_schwerpunkte: []     # z. B. ["ZPO", "ArbGG", "StPO"]
mandate_gleichzeitig: 0     # typische Anzahl aktiver Mandate
risikokalibrierung: ""      # z. B. "konservativ", "ausgewogen", "aggressiv"
seite: ""                   # "Kläger", "Beklagter", "beide"
außenanwälte: false         # Koordination externer Kanzleien?
außenanwalt_liste: []       # externe Kanzleien / Korrespondenzanwälte
haus_stil: ""               # Besonderheiten im Schriftsatzstil
gericht_hauptsächlich: ""   # z. B. "LG Frankfurt", "ArbG München"
berichtsformat: ""          # z. B. "wöchentlich", "nach Bedarf"
outlook_mcp: false          # Outlook MCP verfügbar?
kalender_mcp: false         # Kalender MCP verfügbar?
```

---

## 7. Verfügbare Skills

| Skill | Befehl | Zweck |
|---|---|---|
| Cold-Start-Interview | `/cold-start` | Praxisprofil einrichten |
| Konfiguration anpassen | `/anpassen` | Einzelne Einstellung ändern |
| Neues Mandat | `/mandat-intake` | Mandatsaufnahme |
| Mandats-Update | `/mandat-update [slug]` | Entwicklung dokumentieren |
| Mandats-Briefing | `/mandat-briefing [slug]` | Tiefenbriefing |
| Mandat schließen | `/mandat-schliessen [slug]` | Mandat abschließen |
| Mandat-Workspace | `/mandat-workspace` | Workspace verwalten |
| Portfolio-Status | `/portfolio-status` | Gesamtübersicht |
| Sachverhalts-Chronologie | `/chronologie [slug]` | Zeitstrahl aufbauen |
| Schriftsatzabschnitt | `/schriftsatz [slug]` | Klage, Erwiderung, Berufung |
| Anspruchstabelle | `/anspruchstabelle [slug]` | Element-für-Element-Analyse |
| Mahnschreiben | `/mahnschreiben [slug]` | Vorgerichtliche Aufforderung |
| Mahnschreiben-Intake | `/mahnschreiben-intake` | Vorbereitung Mahnschreiben |
| Eingehendes Schreiben | `/schreiben-eingegangen` | Eingehende Mahnung triage |
| Zeugenvernehmung-Vorbereitung | `/zeuge-vorbereitung [name]` | Vernehmung nach § 373 ff. ZPO |
| Aufbewahrungspflicht | `/beweissicherung [slug]` | Legal Hold nach deutschem Recht |
| Gegenseite-Status | `/gegenseite-status` | Korrespondenz Gegenseite / OC |
| Anwaltsgeheimnis-Prüfung | `/anwaltsgeheimnis [log]` | Beschlagnahmefreiheit prüfen |
| Gerichtl. Vorlage / Zeuge | `/vorlageanordnung` | § 142, 144 ZPO; § 161a StPO |
| Mahnbescheid | `/mahnbescheid` | §§ 688 ff. ZPO |
| Zwangsvollstreckung | `/vollstreckung [slug]` | §§ 704 ff. ZPO |
| Einstweilige Verfügung | `/einstv-verfuegung [slug]` | §§ 935, 940 ZPO |
| Verkehrsunfall | `/verkehrsunfall [slug]` | StVG, § 115 VVG |
| Strafverteidigung Ersttermin | `/strafv-ersttermin [slug]` | StPO, Pflichtverteidigung |
| Streitwert | `/streitwert [slug]` | GKG, RVG |

---

## 8. Fristen und Fristenkalender

Alle fristerzeugenden Ausgaben des Plugins werden mit einer **Fristen-Checkliste** versehen. Das Plugin selbst führt keinen rechtsverbindlichen Fristenkalender. Die verantwortliche Fristenkontrolle obliegt dem bearbeitenden Anwalt (§ 43 BRAO, § 11 BORA).

Kritische Fristen, die das Plugin stets überprüft:
- Klagefrist (§ 167 ZPO i. V. m. § 253 ZPO)
- Berufungsfrist (§ 517 ZPO: 1 Monat)
- Berufungsbegründungsfrist (§ 520 Abs. 2 ZPO: 2 Monate, verlängerbar)
- Revisionsfrist (§ 548 ZPO: 1 Monat)
- Revisionsbegründungsfrist (§ 551 Abs. 2 ZPO: 2 Monate)
- BeschwerdeFrist (§ 569 ZPO: 2 Wochen)
- Widerspruchsfrist Mahnbescheid (§ 692 Abs. 1 Nr. 3 ZPO: 2 Wochen)
- Einspruchsfrist Vollstreckungsbescheid (§ 700 Abs. 1 ZPO: 2 Wochen)
- Verjährung (§§ 195, 199 BGB: Regelmäßig 3 Jahre zum 31.12.)

---

## 9. Mandate und Dateistruktur

```
matters/
├── _log.yaml              # Portfolio-Log aller Mandate
├── [slug]/
│   ├── matter.md          # Mandatsstammdaten
│   └── history.md         # Verlaufsdokumentation
demand-letters/
├── [slug]/
│   ├── intake.md          # Mahnaktion-Intake
│   └── [version].md       # Entwurf
inbound/
├── [JJJJ-MM-TT]-[slug].md # Eingegangene Schreiben
oc-status/
├── [JJJJ-MM-TT]/          # Wöchentliche OC-Statusanfragen
```

---

## 10. Vergütung und Kosten

Alle Vergütungsberechnungen erfolgen nach:
- **RVG** (Rechtsanwaltsvergütungsgesetz) i. V. m. VV RVG (Anlage 1 RVG)
- **GKG** (Gerichtskostengesetz) i. V. m. Anlage 2 GKG
- **FamGKG** für Familiensachen
- **GNotKG** für notarielle Verfahren

Das Plugin gibt Schätzwerte aus, keine rechtsverbindlichen Kostenfestsetzungen. Die Vergütungsvereinbarung (§ 3a RVG) und die Kostenerstattung (§§ 91 ff. ZPO) sind im Einzelfall durch den Anwalt zu prüfen.
