# Megaprompt: lizenzvertragsersteller

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 32 Skills des Plugins `lizenzvertragsersteller`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Anwalts-Dashboard fuer den Lizenzvertragsersteller: Sofort-Triage (IP-Typ, Parteien, Sprache, Rechtswahl), Risiko-Ampel,…
2. **mandat-intake-und-konfliktpruefung** — Mandatsannahme fuer Lizenzvertragsersteller: Konfliktcheck (mehrseitige Vertretung im IP-Verkehr ist Standardrisiko), Ma…
3. **lizenz-geschmacksmuster-design-designg** — Designlizenzen nach DesignG (frueher GeschmacksmusterG): $ 31 DesignG Uebertragung und Lizenz; Eintragung DPMA/EUIPO; Sc…
4. **lizenz-urheberrecht-und-software-urhg** — Urheberrechts- und Software-Lizenzen nach UrhG: $ 31 ff. UrhG einfache und ausschliessliche Nutzungsrechte, $ 32 angemes…
5. **ip-identifikation-und-bestandsaufnahme** — IP-Identifikation und Bestandsaufnahme fuer Lizenzvertraege: Schutzrechtsregister-Auszug, Klassifikation nach Typ (Urheb…
6. **klausel-lizenzgegenstand-und-anlage-ip-liste** — Klausel Lizenzgegenstand mit Anlage A (IP-Liste): pro IP-Typ Identifikation, Schutzrechtsregister-Nummern, Schutzgebiete…
7. **klausel-vertraulichkeit-und-nda-interimsphase** — Vertraulichkeitsklausel im Lizenzvertrag sowie NDA fuer Interimsphase vor Vertragsschluss: Definition vertraulicher Info…
8. **kartellrecht-tt-gvo-eu-316-2014** — Kartellrecht im Lizenzvertrag: TT-GVO VO (EU) 316/2014 Technologietransfer-Gruppenfreistellung; Marktanteilsschwellen 20…
9. **escrow-quellcode-verwahrer-vereinbarung** — Source-Code-Escrow-Vereinbarung: drei-Parteien-Vertrag Lizenzgeber - Lizenznehmer - Escrow-Agent; Hinterlegungsumfang; R…
10. **klausel-haftung-gewaehrleistung-indemnification** — Haftungs- und Gewaehrleistungsklauseln im Lizenzvertrag: Inhaberschaftsgarantie, Patent-Marketability, IP-Infringement-I…
11. **klausel-vertragsdauer-kuendigung-rueckwirkung** — Vertragsdauer-Klauseln: feste Laufzeit, unbefristet mit Kuendigung, Verlaengerungsautomatik (Roll-over), ordentliche und…
12. **steuern-quellensteuer-und-dba-lizenz** — Steuern und Quellensteuer im Lizenzvertrag: $ 49 EStG Quellensteuer auf Royalties 15 Prozent; DBA-Reduktion (z. B. 0 Pro…
13. **lizenz-marke-markeng** — Markenrechtslizenzen nach MarkenG $ 30: Qualitaetskontrolle, Bezeichnungspflicht, Eintragungspflicht im DPMA-Register $ …
14. **output-vertrag-englisch-fertigentwurf** — Output: vollstaendiger Lizenzvertrag in englischer Sprache (Licence Agreement). Standard-Klauseln in English Law / Germa…
15. **lizenz-geschaeftsgeheimnis-knowhow-geschgehg** — Lizenz von Geschaeftsgeheimnissen und Know-how nach GeschGehG: $$ 1-12 GeschGehG; Schutzmassnahmen $ 2 Nr. 1b; Reverse E…

---

## Skill: `einstieg-routing`

_Anwalts-Dashboard fuer den Lizenzvertragsersteller: Sofort-Triage (IP-Typ, Parteien, Sprache, Rechtswahl), Risiko-Ampel, Anschluss-Skill-Router, Norm-Radar, Leitentscheidungs-Anker; maximal eine Rueckfrage._

# Anwalts-Dashboard Lizenzvertragsersteller

> Sie sehen die Sofort-Triage. Keine Rueckfragen, bis die Tabelle steht. Bei klarer Faktenlage gehen wir sofort zum Baukasten — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellpruefung | Standardquelle |
| --- | --- | --- |
| IP-Typ | Urheberrecht/Software · Patent · Marke · Design (GeschmacksmusterG) · Gebrauchsmuster · Geschaeftsgeheimnis/Know-how | Schutzrechtsregister (DPMA, EUIPO, EPA), Vertragsunterlagen |
| Rolle Mandant | Lizenzgeber · Lizenznehmer · Sicherheitengeber · Sicherheitennehmer · Verwahrer (Escrow) · Beide (cross-license) | Mandatsmail, Vollmacht |
| Lizenzumfang | Territorium · Zeit · Anwendungsfeld · exklusiv/non-exklusiv/sole | Geschaeftsmodell, Roadmap |
| Vertragssprache | DE · EN · Bilingual mit Massgebbung | Mandantenwunsch, Gegenseite |
| Rechtswahl | Deutsches Recht · Schweiz · EN&W · NY · Rom-I-VO bei Mehrlaender | Standortverteilung, Vollstreckungsstrategie |
| Vorbefassung | NDA, LOI, MOU schon unterschrieben? | Aktenlage |

## Risiko-Ampel

- **Insolvenz-Risiko Lizenzgeber:** 🔴 bei Software-Abhaengigkeit ohne Escrow · 🟠 bei mittelgrosser Lizenzgeberin · 🟢 etablierter Konzern.
- **Kartellrecht TT-GVO:** 🔴 bei Marktanteil > 30 % (Wettbewerber) bzw. > 20 % (vertikal) · 🟠 bei Schranken-Klauseln (Kernbeschraenkungen) · 🟢 bei reinem KMU.
- **Steuern/Quellensteuer:** 🔴 bei Cross-Border ohne DBA-Pruefung · 🟠 bei DBA mit Quellensteuer-Reduktion · 🟢 bei rein nationaler Lizenz.

## Anschluss-Skills (Router)

| Wenn der Fall traegt … | dann Skill | Erwartung |
| --- | --- | --- |
| IP-Identifikation noch offen | `ip-identifikation-und-bestandsaufnahme` | IP-Inventarliste, Schutzstatus, Belastungen |
| Parteienrollen noch nicht klar | `parteienrolle-klaeren-lizenzgeber-nehmer-sicherheiten-verwahrer` | Rollenmatrix |
| Software-Lizenz | `lizenz-urheberrecht-und-software-urhg` | UrhG-Bausteine, Source-Code-Escrow Hinweis |
| Patent-Lizenz | `lizenz-patent-patg` | PatG-Bausteine, Marktanteils-Check TT-GVO |
| Marke-Lizenz | `lizenz-marke-markeng` | MarkenG, Qualitaetskontrolle, Eintrag DPMA |
| Insolvenzfeste Gestaltung | `insolvenz-fortbestand-paragraf-103-inso-lizenz` + `escrow-quellcode-verwahrer-vereinbarung` | Klausel + Escrow-Mustertext |

**Vorrang:** Wenn IP nicht identifiziert ist, zuerst Skill 2 (Identifikation). Erst danach Klausel-Baukasten.

## Norm-Radar

- **UrhG** §§ 31, 32, 32a (Urheberrechtslizenzen, angemessene Verguetung); § 69a ff. (Software); § 137l UrhG (unbekannte Nutzungsarten)
- **PatG** §§ 9, 15 (Lizenz); § 24 (Zwangslizenz)
- **MarkenG** §§ 30 (Lizenz), 27 (Uebertragung)
- **DesignG** §§ 31 ff.; **GebrMG** §§ 22 ff.
- **GeschGehG** §§ 1-12 (Schutz von Geschaeftsgeheimnissen; Lizenz nach § 3)
- **InsO** § 103 (Wahlrecht des Verwalters bei gegenseitigen Vertraegen)
- **VO (EU) Nr. 316/2014 (TT-GVO)** — Technologietransfer-Gruppenfreistellung
- **Rom-I-VO** Art. 4 (Lizenzvertraege Statut)

## Genau eine Rueckfrage (nur wenn noetig)

> Welcher IP-Typ steht im Vordergrund — und ist der Mandant Lizenzgeber, Lizenznehmer oder beide (Cross-License)?

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie fuehren das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`. Konvention dieses Dashboards: `references/anwalts-dashboard-konvention.md`.

---

## Skill: `mandat-intake-und-konfliktpruefung`

_Mandatsannahme fuer Lizenzvertragsersteller: Konfliktcheck (mehrseitige Vertretung im IP-Verkehr ist Standardrisiko), Mandantenbasisdaten, Ziel- und Eilfristanalyse, Vorvertragspruefung (NDA, LOI, MOU), Dokumenten-Intake-Liste._

# Mandatsannahme und Konfliktpruefung

## Pruefraster

| Punkt | Pruefung | Belege |
| --- | --- | --- |
| Konfliktcheck | Vertretung Gegenseite, Vorbefassung Konzern, Vertretung Wettbewerber im selben Technologiefeld | Kanzleidatenbank, $ 43a BRAO, $ 3 BORA |
| Mandantenbasisdaten | Firma/Anschrift, HRB, gesetzliche Vertreter, UBO | HR-Auszug, Beneficial-Ownership-Register |
| Mandatsumfang | Vertragsentwurf (Lizenzgeber/-nehmer/Cross), Pruefung Vertrag der Gegenseite, Begleitung Verhandlung, Insolvenzberatung | Mandatsmail |
| Zielsetzung | Was soll erreicht werden? Geld, Marktzugang, Insolvenzschutz, Cross-License-Patentaustausch | Klaerung im Erstgespraech |
| Eilfristen | NDA-Verfallsdatum, MOU-Bindungsfristen, Vertragsschlussabsicht | Aktenlage |
| Vorvertraege | NDA, LOI, MOU, Heads of Terms - schon unterschrieben? | Akten |

## Konflikt-Standardrisiken im IP-Verkehr

1. **Mehrseitige Vertretung in einer Lizenzkette** — Lizenzgeber LG vertritt Lizenznehmer LN1, der seinerseits LN2 sublizenziert; eigene Kanzlei darf nicht alle drei vertreten.
2. **Patent-Pool-Lizenzierung** — bei Patent-Pools (FRAND, Standardpatent) ist Vertretung mehrerer Pool-Teilnehmer in der Regel ausgeschlossen.
3. **Wettbewerberkonstellation** — Mandant im Lizenzvertrag heute = Wettbewerber in Patentstreit morgen.

## Dokumenten-Intake (Standardliste)

- Schutzrechtsregister-Auszuege (DPMA, EUIPO, EPA, WIPO; Stand frisch)
- Vorhandene Lizenzvertraege auf dem IP (Vorvergabe? Multiple Licensees?)
- Verpfaendungen, Sicherungsabtretungen
- Konzernabhaengigkeiten (Tochtergesellschaft-IP)
- IP-Klagen (laufend/abgeschlossen)
- NDA-, LOI-, MOU-Volltexte
- Beneficial-Ownership-Register-Auszug (Geldwaeschegesetz)
- DBA-Konstellation bei Cross-Border

## Anschluss

- IP-Identifikation: `ip-identifikation-und-bestandsaufnahme`
- Rollenklaerung: `parteienrolle-klaeren-lizenzgeber-nehmer-sicherheiten-verwahrer`

---

## Skill: `lizenz-geschmacksmuster-design-designg`

_Designlizenzen nach DesignG (frueher GeschmacksmusterG): $ 31 DesignG Uebertragung und Lizenz; Eintragung DPMA/EUIPO; Schutzdauer max 25 Jahre; EU-Gemeinschaftsgeschmacksmuster GGV 6/2002; nicht eingetragenes Gemeinschaftsgeschmacksmuster (3 Jahre Schutz)._

# Lizenz Design (DesignG / EU-Verordnung)

## Normenanker

- DesignG (frueher Geschmacksmustergesetz) - deutsche Designs
- $ 28 DesignG - Schutzdauer max. 25 Jahre (5+5+5+5+5)
- $ 31 DesignG - Uebertragung und Lizenz; analog $ 30 MarkenG
- VO (EG) Nr. 6/2002 GGV - EU-Gemeinschaftsgeschmacksmuster (EUIPO)
- Nicht eingetragenes Gemeinschaftsgeschmacksmuster - 3 Jahre Schutz ab Veroeffentlichung
- Neuheit + Eigenart als Schutzvoraussetzungen

## Spezifika

- **Schutzgegenstand:** zweidimensionale (Muster) oder dreidimensionale (Form) Erscheinungsform; nicht-techisch.
- **Eintragungspflicht:** Im DPMA / EUIPO. Bei nicht eingetragenem GGV: 3 Jahre automatisch.
- **Schutzdauer:** max 25 Jahre nach Anmeldung; alle 5 Jahre verlaengerungspflichtig.
- **Abgrenzung Marke:** Form/Muster, nicht Kennzeichnung; Marke kann zusaetzlich gelten.
- **Abgrenzung Patent:** rein aesthetisch, nicht technisch.

## Klausel-Bausteine (DE)

**1. Lizenzgegenstand Design:**
> "Der Lizenzgeber raeumt dem Lizenznehmer hiermit das [einfache / ausschliessliche] Recht ein, die in **Anlage A** aufgefuehrten eingetragenen Designs ("Lizenzdesigns") fuer die Erzeugnisse [Produkte] im Territorium [Territorium] zu nutzen."

**2. Eintragungs-/Verlaengerungs-Pflicht:**
> "Der Lizenzgeber traegt die Verlaengerungsgebuehren der Lizenzdesigns und sorgt dafuer, dass der Schutz waehrend der Laufzeit dieses Vertrages aufrechterhalten wird."

**3. Verletzungen Dritter:**
> "Der Lizenznehmer informiert den Lizenzgeber unverzueglich ueber Kenntnisnahme von Designverletzungen Dritter. Die Verfolgung erfolgt durch den Lizenzgeber; bei nicht-Verfolgung erhaelt der Lizenznehmer ein subsidiaeres Klagerecht."

## Anschluss

- IP-Identifikation: `ip-identifikation-und-bestandsaufnahme`
- Verguetung: `klausel-verguetung-pauschale-royalty-tiered`

---

## Skill: `lizenz-urheberrecht-und-software-urhg`

_Urheberrechts- und Software-Lizenzen nach UrhG: $ 31 ff. UrhG einfache und ausschliessliche Nutzungsrechte, $ 32 angemessene Verguetung, $ 32a Bestseller-Klausel, $ 69a-g UrhG Computerprogramme, $ 137l UrhG unbekannte Nutzungsarten. Mit Klauselbausteinen._

# Lizenz Urheberrecht / Software ($$ 31 ff. UrhG)

## Normenanker

- $ 31 UrhG - Einraeumung von Nutzungsrechten (einfach vs. ausschliesslich)
- $ 31a UhG - Vertraege ueber unbekannte Nutzungsarten
- $ 32 UrhG - angemessene Verguetung (Anspruch des Urhebers)
- $ 32a UrhG - weitere Beteiligung des Urhebers (Bestseller-Klausel; $ 32a Abs. 2 fuer Dritte)
- $ 35 UrhG - Einraeumung weiterer Nutzungsrechte (Sub-Lizenz)
- $ 40 UrhG - Vertraege ueber kuenftige Werke
- $ 41 UrhG - Rueckrufsrecht wegen Nichtausuebung
- $ 42 UrhG - Rueckrufsrecht wegen gewandelter Ueberzeugung
- $$ 69a-g UrhG - Schutz von Computerprogrammen (Sonderrecht)

## Lizenzformen

| Typ | Definition | Klauselbeispiel |
|---|---|---|
| einfaches Nutzungsrecht | $ 31 Abs. 2 UrhG; nicht-exklusiv | "Der Lizenzgeber raeumt dem Lizenznehmer das einfache Nutzungsrecht ein…" |
| ausschliessliches Nutzungsrecht | $ 31 Abs. 3 UrhG; exklusiv | "ausschliessliches Nutzungsrecht, beschraenkt auf [Territorium/Zeit/Feld]" |
| zeitlich beschraenkt | $ 31 Abs. 1 S. 2 UrhG | Konkrete Laufzeit mit Verlaengerungsklausel |
| raeumlich beschraenkt | $ 31 Abs. 1 S. 2 UrhG | Land/Region/Sprachraum |
| inhaltlich beschraenkt | $ 31 Abs. 1 S. 2 UrhG (Zweckuebertragungstheorie) | Konkrete Nutzungsart benennen |

## Pflichten und Schranken

- **Zweckuebertragungstheorie ($ 31 Abs. 5 UrhG):** Im Zweifel nur die Rechte, die fuer den Vertragszweck erforderlich sind. → Im Vertrag konkrete Nutzungsarten aufzaehlen.
- **Angemessenheits-Korrektur ($ 32 UrhG):** Urheber hat Anspruch auf nachtraegliche Anpassung der Verguetung; nicht abdingbar (zwingend).
- **Bestsellerparagraf ($ 32a UrhG):** Bei auffaelligem Missverhaeltnis nachtraeglicher Korrekturanspruch; auch gegen Lizenznehmer-Sub-Lizenznehmer in der Kette.

## Software-Spezifika ($$ 69a-g UrhG)

| Norm | Inhalt |
|---|---|
| $ 69a | Schutzfaehigkeit von Computerprogrammen; Ausdrucksform |
| $ 69b | Arbeitsergebnis des Arbeitnehmers - AG erwirbt ausschliessliche Nutzungsrechte kraft Gesetzes |
| $ 69c | Zustimmungsbeduerftige Handlungen (Vervielfaeltigung, Umarbeitung, Verbreitung) |
| $ 69d | Erlaubte Handlungen ohne Zustimmung (bestimmungsgemaesse Benutzung, Sicherheitskopie) |
| $ 69e | Dekompilierung zur Interoperabilitaet |
| $ 69f | Verletzungsfolgen |
| $ 69g | Verhaeltnis zu sonstigen Vorschriften |

## Source-Code vs. Object-Code

- **Object-Code-Lizenz** (Standard): nur Ausfuehrung, keine Quellcode-Einsicht.
- **Source-Code-Lizenz** (selten direkt): mit Recht zur Bearbeitung; meist nur als Escrow.
- → Bei Software-Abhaengigkeit: Source-Code-Escrow vereinbaren (siehe `escrow-quellcode-verwahrer-vereinbarung`).

## Open-Source-Compliance

Pruefen vor Vertragsschluss:
- Open-Source-Bill-of-Materials (OSS-BOM): welche Komponenten sind im Stack?
- Copyleft-Risiken: GPL, AGPL → Quellcode-Offenlegungspflicht?
- LGPL: dynamisches Linking unproblematisch fuer Distribution.
- MIT/Apache-2.0: zulaessige Mischung.
- Lizenzkompatibilitaet $ 69c UrhG; bei GPL-Verstoss: Loeschung der OSS-Komponente vor Distribution.

## Klausel-Bausteine (DE)

**1. Lizenzgegenstand:**
> "Der Lizenzgeber raeumt dem Lizenznehmer hiermit das [einfache / ausschliessliche] Nutzungsrecht an der in **Anlage A** bezeichneten Software ("Lizenzgegenstand") fuer die in **Anlage B** definierten Nutzungsarten ein."

**2. Nutzungsarten:**
> "Die Lizenz umfasst die Vervielfaeltigung im Sinne des $ 69c Nr. 1 UrhG, die bestimmungsgemaesse Benutzung im Sinne des $ 69d Abs. 1 UrhG sowie [Verbreitung / Bearbeitung / oeffentliche Wiedergabe]."

**3. Verguetung:**
> "Die Verguetung betraegt [Pauschale / Running Royalty in Hoehe von X % des Nettoumsatzes]. Die Parteien bestaetigen, dass die Verguetung im Sinne des $ 32 UrhG angemessen ist."

## Anschluss

- Source-Code-Escrow: `escrow-quellcode-verwahrer-vereinbarung`
- Verguetungsklausel: `klausel-verguetung-pauschale-royalty-tiered`
- Insolvenz: `insolvenz-fortbestand-paragraf-103-inso-lizenz`

---

## Skill: `ip-identifikation-und-bestandsaufnahme`

_IP-Identifikation und Bestandsaufnahme fuer Lizenzvertraege: Schutzrechtsregister-Auszug, Klassifikation nach Typ (Urheber Patent Marke Design Gebrauchsmuster Geschaeftsgeheimnis), Belastungen, Erfindervergutung, Lizenzhistorie, IP-Inventar als Anlage A._

# IP-Identifikation und Bestandsaufnahme

## Zweck

Ohne saubere IP-Identifikation kein guter Lizenzvertrag. Dieser Skill liefert die IP-Inventur fuer die Anlage A des Vertrags.

## IP-Typen — pro Typ ein Register

| IP-Typ | Register / Quelle | Pruefen |
| --- | --- | --- |
| Urheberrecht (klassische Werke) | nicht registriert; Werk-Nachweis | Schoepfungsdatum, Werkkategorie, Schoepfer/Miturheber, ggf. Verwertungsgesellschaft |
| Software | nicht registriert; Repository-Historie | Repository-Standort (GitHub etc.), Mitarbeiter-Code-Anteile $ 69b UrhG, Open-Source-Komponenten |
| Patent | DPMA (deutsch), EPA (europaeisch), USPTO/WIPO | Anmeldedatum, Erteilungsdatum, Schutzdauer, Erfinder, Gemeinschaft, Arbeitnehmererfindergesetz |
| Marke | DPMA, EUIPO, WIPO | Reg.-Nr., Wort/Bild, Klassen, Schutzgebiete, Verlaengerung, Benutzungspflicht |
| Geschmacksmuster (Design) | DPMA, EUIPO | Reg.-Nr., Anmeldedatum, Schutzdauer (max 25 J.) |
| Gebrauchsmuster | DPMA | Reg.-Nr., Anmeldedatum, Schutzdauer 10 J., kein Pruefverfahren |
| Geschaeftsgeheimnis/Know-how | nicht registriert; Schutzmassnahmen | Schutzmassnahmen nach $ 2 GeschGehG (NDAs, Zugriffsbeschraenkung, Branch-Protection) |
| Domains | Whois / united-domains | Inhaber, Provider, Verlaengerung |

## Inventar-Schema (Anlage A des Vertrags)

```
| Asset-Nr. | Bezeichnung | IP-Typ | Reg.-Nr. | Schutzgebiet | Anmelder/Inhaber | Klassen | Status | Belastungen |
```

Pro Zeile: ein Schutzrecht. Belastungen = Lizenzen Dritter, Pfandrechte, Sicherungsabtretungen, Veroeffentlichungen die Patentschutz gefaehrden.

## Pruefroutine

1. **Bestand:** Sind alle Schutzrechte tatsaechlich auf den Lizenzgeber registriert?
2. **Lebensdauer:** Restschutzdauer, Verlaengerungspflichten, Gebuehren faellig?
3. **Belastungen:** Lizenzen Dritter, Verpfaendungen, Sicherungsabtretungen?
4. **Erfindervergutung:** Bei Patenten - Arbeitnehmererfindergesetz $ 9 ArbnErfG; Verguetung an Erfinder schon abgeloest?
5. **Drittstaaten:** Schutz in den Lizenzgebieten wirklich vorhanden? (insb. US/CN/JP)
6. **Mitinhaber:** Bei Miturheberschaft oder Patentgemeinschaft: alle erfasst?
7. **OSS-Compliance:** Bei Software - Open-Source-Komponenten erfasst, Lizenzkompatibilitaet $ 69c UrhG?

## Hinweis bei Software

- $ 69a UrhG schuetzt Computerprogramme als Werke.
- $ 69b UrhG: Arbeitsergebnis des AN gehoert kraft Gesetzes dem AG (ausschliessliche Nutzungsrechte).
- Pruefen: Welche Repositories? Welche Branches? Wer ist Owner? Welche Open-Source-Lizenzen sind im Stack?

## Anschluss

- Pro IP-Typ vertiefen: `lizenz-urheberrecht-und-software-urhg`, `lizenz-patent-patg`, `lizenz-marke-markeng`, `lizenz-geschmacksmuster-design-designg`, `lizenz-gebrauchsmuster-gebrmg`, `lizenz-geschaeftsgeheimnis-knowhow-geschgehg`.

---

## Skill: `klausel-lizenzgegenstand-und-anlage-ip-liste`

_Klausel Lizenzgegenstand mit Anlage A (IP-Liste): pro IP-Typ Identifikation, Schutzrechtsregister-Nummern, Schutzgebiete, Lebensdauer, Belastungen; mit Praezisierungstechniken (Patente per Anspruch, Marken per Nizza-Klasse, Software per Repository-Hash)._

# Klausel Lizenzgegenstand + Anlage A

## Funktion

Praezision schlaegt Generalformulierung. Wer den Lizenzgegenstand vage haelt ("alle IP, die der Lizenzgeber besitzt"), riskiert spaeter Streit ueber Zugehoerigkeit.

## Praezisierungstechniken pro IP-Typ

| IP-Typ | Identifikation |
|---|---|
| Urheberrecht (Werk) | Titel, Schoepfer, Schoepfungsjahr, Werkkategorie |
| Software | Repository-URL, Commit-Hash (z. B. SHA), Branch-Name, Build-Version |
| Patent | Reg.-Nr. + Datum + ggf. Anspruchsnummer |
| Marke | Reg.-Nr., Wortmarke/Bildmarke, Nizza-Klassen |
| Design | Reg.-Nr., Beschreibung, Schutzgebiete |
| Gebrauchsmuster | Reg.-Nr., Datum |
| Geschaeftsgeheimnis | Bezeichnung + Anlage-Hash + Versionsnummer |
| Domain | Domain + Registrar |

## Anlage-A-Schema (Standard)

```
ANLAGE A — LIZENZGEGENSTAND
==========================

A.1 Patente

| Nr. | Reg.-Nr. | Schutzgebiet | Anmeldedatum | Status | Erfinder | Lizenzansprueche |
|-----|----------|--------------|--------------|--------|----------|-------------------|

A.2 Marken

| Nr. | Reg.-Nr. | Wort/Bild | Nizza-Klassen | Schutzgebiete | Verlaengerung | Status |
|-----|----------|-----------|---------------|---------------|---------------|--------|

A.3 Software

| Nr. | Repository | Commit-Hash | Branch | Build-Version | Vergebene Sublizenzen |
|-----|-----------|-------------|--------|---------------|----------------------|

A.4 Know-how

| Nr. | Bezeichnung | Anlage-Hash | Versionsnummer | Schutzmassnahmen |
|-----|-------------|-------------|----------------|------------------|
```

## Klausel-Baustein

> **$ 2 Lizenzgegenstand.**
>
> (1) Lizenzgegenstand sind die in **Anlage A** aufgefuehrten Schutzrechte und das in Anlage A definierte Know-how (gemeinsam "Lizenzgegenstand").
>
> (2) Etwaige Anspruchserweiterungen, Patentanmeldungen aus derselben Erfindung oder Folgeanmeldungen fallen [JA / NEIN] automatisch unter den Lizenzgegenstand. Bei JA: Aktualisierung Anlage A jaehrlich.
>
> (3) Anlage A ist integraler Bestandteil dieses Vertrages.

## Pruefroutine vor Vertragsschluss

1. Schutzrechtsregister live abfragen (DPMA, EUIPO, EPA)
2. Whois fuer Domains
3. Repository-Hash bei Software (z. B. `git log -1 --pretty="%H"`)
4. Anlage-Hash bei Know-how (SHA-256 der Dokumentensammlung)
5. Belastungen pro Schutzrecht eintragen

## Anschluss

- IP-Identifikation: `ip-identifikation-und-bestandsaufnahme`
- Lizenzumfang: `klausel-lizenzumfang-territorium-zeit-feld`

---

## Skill: `klausel-vertraulichkeit-und-nda-interimsphase`

_Vertraulichkeitsklausel im Lizenzvertrag sowie NDA fuer Interimsphase vor Vertragsschluss: Definition vertraulicher Informationen, Ausnahmen (oeffentlich, schon bekannt), Dauer (5 Jahre nach Vertragsende), Beweislast, Rueckgabepflicht, vertragsstrafen._

# Klausel Vertraulichkeit + NDA-Interimsphase

## Zweck

Bei Lizenzverhandlungen werden Geschaeftsgeheimnisse, Patentinformationen, Roadmaps offengelegt. Schutz erforderlich.

## Interim-NDA (vor Vertragsschluss)

Standardtext fuer die Verhandlungs-/DD-Phase:

> **Non-Disclosure Agreement / Vertraulichkeitsvereinbarung**
>
> 1. Die Parteien beabsichtigen, ueber den Abschluss eines Lizenzvertrages zu verhandeln. Zu diesem Zweck tauschen sie vertrauliche Informationen aus.
> 2. "Vertrauliche Information" bezeichnet alle technischen, kommerziellen, finanziellen oder organisatorischen Informationen, die als vertraulich gekennzeichnet sind oder erkennbar geheim sein sollen.
> 3. Empfaenger verwendet vertrauliche Informationen ausschliesslich zum Zweck der Pruefung einer moeglichen Lizenz; gibt sie nur an Mitarbeiter und Berater weiter, die einer Geheimhaltungspflicht unterliegen ("need to know").
> 4. Ausnahmen: oeffentlich bekannte Informationen, vor Offenlegung bereits dem Empfaenger bekannte Informationen, von Dritten ohne Geheimhaltungspflicht erhaltene Informationen, durch eigene Entwicklung unabhaengig erworbene Informationen.
> 5. Laufzeit: 24 Monate ab Unterzeichnung. Geheimhaltungspflicht besteht zusaetzlich 5 Jahre fort.
> 6. Bei Vertragsschluss eines Lizenzvertrages tritt dieser an die Stelle des NDA; bei Nichtzustandekommen besteht das NDA fort.
> 7. Vertragsstrafe bei Verstoss: [Betrag] EUR pro Fall.

## Vertraulichkeitsklausel im Lizenzvertrag

> **$ 13 Vertraulichkeit.**
>
> (1) Beide Parteien verpflichten sich, alle im Zusammenhang mit diesem Vertrag erhaltenen vertraulichen Informationen der jeweils anderen Partei geheim zu halten.
>
> (2) "Vertrauliche Information" bezeichnet alle technischen, kommerziellen, finanziellen, geschaeftlichen, personellen, wissenschaftlichen oder organisatorischen Informationen, die als vertraulich gekennzeichnet oder erkennbar geheimhaltungsbeduerftig sind. Dies umfasst insbesondere den Lizenzgegenstand, Anlage A, Royalty-Hoehen, Audit-Berichte, Sub-Lizenz-Konditionen, Roadmap-Informationen.
>
> (3) Ausnahmen: Eine Information ist nicht vertraulich, wenn sie
>   a) oeffentlich bekannt ist oder waehrend der Laufzeit dieses Vertrages ohne Verschulden der empfangenden Partei oeffentlich wird;
>   b) der empfangenden Partei bereits vor Erhalt nachweislich bekannt war;
>   c) von einem Dritten ohne Geheimhaltungspflicht uebermittelt wurde;
>   d) unabhaengig von der empfangenden Partei entwickelt wurde.
>
> (4) Geheimhaltungspflicht ueber das Vertragsende hinaus: 5 Jahre.
>
> (5) Bei Verstoss schuldet die verletzende Partei der anderen eine Vertragsstrafe in Hoehe von [Betrag] EUR pro Verstoss, hoechstens [Maximalbetrag] pro Jahr. Weitergehende Schadensersatzansprueche bleiben unberuehrt.

## Anschluss

- Geschaeftsgeheimnis-Lizenz: `lizenz-geschaeftsgeheimnis-knowhow-geschgehg`
- Datenschutz: `datenschutz-dsgvo-im-lizenzvertrag`

---

## Skill: `kartellrecht-tt-gvo-eu-316-2014`

_Kartellrecht im Lizenzvertrag: TT-GVO VO (EU) 316/2014 Technologietransfer-Gruppenfreistellung; Marktanteilsschwellen 20 / 30 Prozent; Kernbeschraenkungen Art. 4; nicht-freigestellte Beschraenkungen Art. 5; Schranken bei vertikalen Vertraegen._

# Kartellrecht — TT-GVO (EU) 316/2014

## Normenanker

- VO (EU) Nr. 316/2014 - Technologietransfer-Gruppenfreistellungsverordnung (TT-GVO)
- Art. 101 AEUV - Kartellverbot
- Art. 101 Abs. 3 AEUV - Freistellungsmoeglichkeit
- Leitlinien zur TT-GVO (2014/C 89/03)

## Anwendbarkeit

TT-GVO gilt fuer **Technologietransfer-Vereinbarungen**: Lizenzvertraege, die Patente, Know-how, Designs oder Software (im Zusammenhang mit Patenten/Know-how) zum Gegenstand haben.

→ Kombinierte Lizenz Patent + Know-how + Marke: TT-GVO greift.
→ Reine Marken-/Urheberrechts-Lizenzen: Vertikal-GVO statt TT-GVO.

## Marktanteilsschwellen (Art. 3 TT-GVO)

| Konstellation | Schwelle |
|---|---|
| **Wettbewerber** (gleiche relevante Maerkte) | gemeinsam ≤ 20 % |
| **Nicht-Wettbewerber** (vertikal) | jeweils ≤ 30 % |

Bei Ueberschreiten: Einzelfall-Pruefung nach Art. 101 III AEUV; keine automatische Freistellung.

## Kernbeschraenkungen Art. 4 TT-GVO ("Schwarze Liste")

Bei diesen Klauseln entfaellt die Freistellung **vollstaendig**:

| Klausel | Verbot |
|---|---|
| Preisbindung Lizenznehmer | Preise fuer Lizenzprodukte vorgeschrieben |
| Quotenbeschraenkung Lizenznehmer | Mengenbeschraenkung (mit Sonderregeln) |
| Beschraenkung passive Verkaeufe | Lizenznehmer darf nicht auf unaufgefordert Bestellungen reagieren |
| Marktaufteilung Wettbewerber | Markt aufteilen (mit Ausnahmen fuer exklusive Lizenz) |

## Nicht freigestellte Beschraenkungen Art. 5 TT-GVO ("Graue Liste")

Diese Klauseln verlieren die Freistellung, **andere Vertragsteile bleiben** freigestellt:

1. **Exklusives Grant-Back** auf nicht-abtrennbare Verbesserungen des Lizenznehmers
2. **Non-Challenge-Klausel** (Verbot Schutzrechtsangriff)
3. Bei Vertraegen zwischen Nicht-Wettbewerbern: Beschraenkung der Lizenznehmer-Forschung in einem nicht-lizenzierten Field

## Praktische Pruefroutine

```
1. IP-Typ pruefen: TT-GVO oder Vertikal-GVO?
2. Marktanteilsschwelle pruefen: 20 % / 30 %?
3. Klausel-Liste durchgehen: Kernbeschraenkungen (Art. 4)?
4. Grenze gegen Grant-Back, Non-Challenge (Art. 5)?
5. Bei Marktanteil-Ueberschreitung: Einzelfall-Pruefung Art. 101 III AEUV.
```

## Klausel-Bausteine

**A. Compliance-Bestaetigung:**
> "Die Parteien sind sich einig, dass dieser Vertrag in Uebereinstimmung mit der TT-GVO (VO (EU) Nr. 316/2014) gestaltet ist. Sollte einzelne Klauseln gegen Art. 4 oder 5 TT-GVO verstossen, vereinbaren die Parteien deren Anpassung, ohne die Wirksamkeit der uebrigen Klauseln zu beruehren ($ 139 BGB)."

**B. Non-Challenge mit Kuendigungsrecht (sicherer Ersatz fuer Verbot):**
> "Sollte der Lizenznehmer die Gueltigkeit eines Lizenzschutzrechts angreifen, ist der Lizenzgeber zur ausserordentlichen Kuendigung berechtigt."

**C. Aktives vs. passives Gebietsschutz:**
> "Der Lizenznehmer wird in einem ihm zugewiesenen exklusiven Gebiet aktive Verkaeufe nicht anbieten. Passive Verkaeufe (Reaktion auf unaufgeforderte Anfragen) bleiben jederzeit zulaessig."

## Anschluss

- Verbesserungen: `klausel-verbesserungen-grant-back`
- Exklusivitaet: `klausel-exklusivitaet-sole-non-exclusive`

---

## Skill: `escrow-quellcode-verwahrer-vereinbarung`

_Source-Code-Escrow-Vereinbarung: drei-Parteien-Vertrag Lizenzgeber - Lizenznehmer - Escrow-Agent; Hinterlegungsumfang; Release-Trigger (Insolvenz, Wartungsausfall); Aktualisierungspflicht; bekannte Escrow-Anbieter; insolvenzfeste Gestaltung._

# Escrow / Quellcode-Verwahrer-Vereinbarung

## Anwendungsfall

Lizenznehmer macht sich von der Software des Lizenzgebers abhaengig. Bei Ausfall des Lizenzgebers (Insolvenz, Geschaeftsaufgabe) braucht der Lizenznehmer Zugriff auf Source Code, um den Betrieb fortzufuehren. Loesung: Drei-Parteien-Escrow-Vertrag.

## Drei-Parteien-Struktur

```
+---------------+            +---------------+
|  Lizenzgeber  | <--------> |  Lizenznehmer |
+---------------+            +---------------+
        |                            ^
        | Hinterlegung               | Release bei Trigger
        v                            |
        +-------- Escrow-Agent ------+
                  (Verwahrer)
```

## Hinterlegungsumfang

| Bestandteil | Inhalt |
|---|---|
| **Source Code** | Vollstaendiger lauffaehiger Quellcode (Git-Bundle mit Commit-Historie) |
| **Build-Anweisungen** | Wie wird aus Source Code ein Build erstellt? Konfigurationsdateien, Build-Scripts |
| **Dependencies-Liste** | OSS und proprietaere Abhaengigkeiten mit Versionen |
| **Dokumentation** | Architektur-Diagramme, API-Docs, Datenbank-Schema |
| **Schluessel/Credentials** | (falls fuer Build noetig) |
| **Test-Suiten** | Automatisierte Tests + Erwartete Ergebnisse |

## Release-Trigger

| Trigger | Definition |
|---|---|
| **Insolvenz Lizenzgeber** | Antrag auf Insolvenzeroeffnung; Geschaeftseinstellung |
| **Wartungsausfall** | Nicht-Erfuellung der Wartungs-/Support-Pflicht waehrend > 90 Tagen |
| **Schwere Vertragsverletzung** | Z. B. Verletzung des Lizenzgegenstands oder Insolvenzanmeldung |
| **Verkauf Lizenzgeber** | Verkauf des IP an Dritten ohne Fortfuehrung Wartung |

## Anbieter (Beispiele, marktueblich)

- **Iron Mountain** (Marktfuehrer, USA + Europa)
- **NCC Group** (UK, mit Verification-Services)
- **Escrow Europe** (Niederlande)
- **Deutscher Anwalts-/Notarverwahrer** (kleine Vertragsvolumina)

## Aktualisierungspflicht

> "Der Lizenzgeber hinterlegt einen aktualisierten Source Code mindestens vierteljaehrlich. Bei wesentlichen Aenderungen (neue Major-Version) Aktualisierung unverzueglich."

## Verification-Klausel

> "Der Lizenznehmer hat das Recht, einmal pro Jahr durch den Escrow-Agent eine technische Verifikation durchzufuehren: Build aus dem hinterlegten Code reproduzieren und mit der Lizenzversion vergleichen. Die Verifikationskosten traegt der Lizenznehmer."

## Insolvenzfeste Gestaltung

Damit der Verwalter den Escrow nicht "abwaehlen" kann ($ 103 InsO):

1. Source Code befindet sich **rechtlich beim Lizenznehmer** mit aufschiebender Bedingung
2. Hinterlegung beim Escrow-Agent dient nur der Realisierung
3. Trigger-Tatbestand "Insolvenz" als Release-Bedingung

Siehe vertiefend: `insolvenz-fortbestand-paragraf-103-inso-lizenz`.

## Klausel-Baustein

> **$ 14 Source-Code-Escrow.**
>
> (1) Der Lizenzgeber wird den vollstaendigen Source Code zur Lizenzsoftware nebst Build-Anweisungen, Dependencies-Liste, Architektur-Dokumentation und Test-Suite bei einem Escrow-Agent ("Verwahrer") hinterlegen. Verwahrer wird einvernehmlich von den Parteien innerhalb von 30 Tagen nach Vertragsunterzeichnung bestimmt.
>
> (2) Der Lizenzgeber aktualisiert die Hinterlegung mindestens vierteljaehrlich.
>
> (3) Der Verwahrer gibt die Hinterlegung an den Lizenznehmer heraus, wenn einer der folgenden Trigger eintritt: (a) Eroeffnung eines Insolvenzverfahrens ueber das Vermoegen des Lizenzgebers; (b) Wartungsausfall ueber mehr als 90 zusammenhaengende Tage trotz schriftlicher Mahnung; (c) endgueltige Geschaeftsaufgabe des Lizenzgebers.
>
> (4) Mit Herausgabe erwirbt der Lizenznehmer das Recht, den Source Code zu nutzen, zu modifizieren und zur Wartung der Lizenzsoftware einzusetzen. Eine Weitergabe an Dritte ist ausgeschlossen.
>
> (5) Die Kosten des Escrow traegt [der Lizenzgeber / der Lizenznehmer / die Parteien je zur Haelfte].

## Anschluss

- Insolvenzfestigkeit: `insolvenz-fortbestand-paragraf-103-inso-lizenz`
- Software-Lizenz: `lizenz-urheberrecht-und-software-urhg`

---

## Skill: `klausel-haftung-gewaehrleistung-indemnification`

_Haftungs- und Gewaehrleistungsklauseln im Lizenzvertrag: Inhaberschaftsgarantie, Patent-Marketability, IP-Infringement-Indemnification, Haftungshoechstgrenzen, Ausschluesse fuer Vorsatz und grobe Fahrlaessigkeit, Drittansprueche._

# Klausel Haftung, Gewaehrleistung, Indemnification

## Drei Pflichtbausteine

### A. Inhaberschaftsgarantie (Title Warranty)

Lizenzgeber garantiert, dass:
1. Lizenzgegenstand existiert
2. Lizenzgeber alleiniger / berechtigter Inhaber ist
3. Keine Drittrechte entgegen stehen
4. Keine schwebenden Klagen / Aufhebungsverfahren

> "$ 8 Garantien des Lizenzgebers.
> (1) Der Lizenzgeber garantiert, dass er alleiniger Inhaber des Lizenzgegenstands ist (mit Ausnahme der in **Anlage A** gekennzeichneten Mitinhaberschaften).
> (2) Der Lizenzgegenstand ist frei von Rechten Dritter, soweit dem Lizenzgeber nach pflichtgemaesser Pruefung bekannt.
> (3) Keine Drittrechts-Klage oder Loeschungsverfahren ist anhaengig."

### B. IP-Infringement-Indemnification

Was passiert, wenn ein Dritter die Nutzung des Lizenzgegenstands durch den Lizenznehmer als Verletzung seines eigenen Schutzrechts angreift?

> "(4) Wird der Lizenznehmer von einem Dritten wegen Verletzung von Schutzrechten in Anspruch genommen, die sich aus der Nutzung des Lizenzgegenstands ergeben sollen, hat der Lizenzgeber den Lizenznehmer von solchen Anspruechen freizustellen, soweit die Verletzungshandlung im Rahmen des vertragsgemaessen Gebrauchs liegt und der Lizenznehmer den Lizenzgeber unverzueglich informiert."

### C. Haftungshoechstgrenzen

Bei B2B-Vertraegen ueblich:

> "$ 9 Haftungsbeschraenkungen.
> (1) Die Haftung des Lizenzgebers fuer einfache Fahrlaessigkeit ist je Vertragsjahr auf einen Betrag in Hoehe der im jeweiligen Vertragsjahr gezahlten Lizenzgebuehren begrenzt; insgesamt jedoch nicht weniger als [Betrag] EUR.
> (2) Mittelbare Schaeden, Folgeschaeden, entgangener Gewinn und reine Vermoegensschaeden sind ausgeschlossen.
> (3) Diese Beschraenkungen gelten nicht bei Vorsatz, grober Fahrlaessigkeit, der Verletzung von Leben, Koerper oder Gesundheit sowie bei Verletzung wesentlicher Vertragspflichten ("Kardinalpflichten")."

## Spezialfall Patent Validity

Bei Patentlizenzen kommt hinzu: Was bei Patent-Nichtigerklaerung?
- Lizenznehmer hat Anspruch auf Erstattung gezahlter Lizenzgebuehren? → meist nicht (Risikoteilung).
- Empfehlung: ausdrueckliche Risikozuweisung.

> "Sofern ein Lizenzpatent durch rechtskraeftiges Urteil nichtig erklaert wird, endet die Lizenz fuer dieses Patent mit dem Tag der Rechtskraft. Bereits gezahlte Lizenzgebuehren werden nicht erstattet."

## Spezialfall Software Bug-Indemnification

> "Der Lizenzgeber gewaehrleistet, dass die Software im Wesentlichen den in **Anlage C** beschriebenen Funktionen entspricht. Bei wesentlichen Maengeln kann der Lizenznehmer Nachbesserung innerhalb von 30 Tagen verlangen."

## Anschluss

- Vertragsdauer: `klausel-vertragsdauer-kuendigung-rueckwirkung`
- Insolvenz: `insolvenz-fortbestand-paragraf-103-inso-lizenz`

---

## Skill: `klausel-vertragsdauer-kuendigung-rueckwirkung`

_Vertragsdauer-Klauseln: feste Laufzeit, unbefristet mit Kuendigung, Verlaengerungsautomatik (Roll-over), ordentliche und ausserordentliche Kuendigung, Folgen Beendigung (Rueckgabe, Vertraulichkeit ueberhang, Lizenz-Nachwirkung)._

# Klausel Vertragsdauer und Kuendigung

## Vier Laufzeitmodelle

| Modell | Beschreibung |
|---|---|
| **Fest** | "5 Jahre", danach Ende |
| **Fest + Rollover** | "5 Jahre, dann jeweils 1 Jahr ohne Kuendigung 6 Monate vor Ablauf" |
| **Unbefristet mit Kuendigung** | "auf unbestimmte Zeit mit ordentlicher Kuendigung mit 12 Monaten Frist zum Jahresende" |
| **Schutzrechtsabhaengig** | "bis zum Ablauf des letzten Lizenzpatents" |

## Klausel-Bausteine

**A. Feste Laufzeit:**
> "$ 11 Vertragsdauer.
> (1) Dieser Vertrag hat eine Laufzeit von [N] Jahren ab dem [Wirksamkeitsdatum]. Er endet automatisch mit Ablauf der Laufzeit, ohne dass es einer Kuendigung bedarf."

**B. Rollover:**
> "(2) Die Laufzeit verlaengert sich um jeweils [M] Jahre, sofern keine Partei spaetestens [F] Monate vor Ablauf der jeweiligen Laufzeit dem Vertrag schriftlich widerspricht."

**C. Ausserordentliche Kuendigung:**
> "(3) Beide Parteien koennen den Vertrag aus wichtigem Grund ohne Einhaltung einer Kuendigungsfrist kuendigen. Ein wichtiger Grund liegt insbesondere vor bei:
> - wesentlicher Vertragsverletzung, die trotz schriftlicher Abmahnung nicht binnen 30 Tagen behoben wird,
> - Verzug mit Lizenzzahlungen ueber 60 Tage,
> - Eroeffnung eines Insolvenzverfahrens ueber das Vermoegen der Gegenseite,
> - Verletzung der Vertraulichkeitspflicht,
> - dauerhafter Nichtnutzung der Lizenz (bei ausschliesslicher Lizenz, mehr als 24 Monate)."

**D. Folgen Beendigung:**
> "$ 12 Folgen der Vertragsbeendigung.
> (1) Mit Vertragsende erloeschen alle Nutzungsrechte des Lizenznehmers.
> (2) Der Lizenznehmer ist verpflichtet, binnen 30 Tagen alle koerperlichen und elektronischen Kopien des Lizenzgegenstands zurueckzugeben oder nachweislich zu vernichten.
> (3) Vorhandene Bestaende von Lizenzprodukten duerfen waehrend einer Auslaufphase von [X] Monaten weiter abverkauft werden ('sell-off-period'); Lizenzgebuehren werden weiter gezahlt.
> (4) Die Vertraulichkeitspflicht ($ 13) gilt 5 Jahre ueber das Vertragsende hinaus fort.
> (5) Verguetungsrueckforderungen sind ausgeschlossen, soweit nicht ausdruecklich anders geregelt."

**E. Lizenz-Nachwirkung bei Sub-Lizenzen:**
> "(6) Sub-Lizenzen erloeschen mit der Hauptlizenz, soweit die Sub-Lizenznehmer nicht binnen 30 Tagen nach Vertragsende einen unmittelbaren Lizenzvertrag mit dem Lizenzgeber abschliessen."

## Anschluss

- Vertraulichkeit: `klausel-vertraulichkeit-und-nda-interimsphase` (folgt in Teil D)
- Insolvenz: `insolvenz-fortbestand-paragraf-103-inso-lizenz`

---

## Skill: `steuern-quellensteuer-und-dba-lizenz`

_Steuern und Quellensteuer im Lizenzvertrag: $ 49 EStG Quellensteuer auf Royalties 15 Prozent; DBA-Reduktion (z. B. 0 Prozent DE-USA mit Antrag); EU-Zinsen-Lizenzgebuehren-Richtlinie; Umsatzsteuer auf Lizenzen; Gross-up-Klauseln._

# Steuern und Quellensteuer — Lizenz

## Drei Steuerthemen

### A. Quellensteuer auf Royalties

| Norm | Inhalt |
|---|---|
| $ 49 I Nr. 6 EStG | Lizenzgebuehren an beschraenkt steuerpflichtige Auslaender: Quellensteuer 15 % |
| $ 50a EStG | Steuerabzug an der Quelle; Schuldner = Lizenznehmer |
| $ 50d EStG | Erstattungs-/Freistellungsverfahren beim Bundeszentralamt fuer Steuern (BZSt) |

### B. DBA-Reduktion

Doppelbesteuerungsabkommen reduzieren regelmaessig die Quellensteuer:

| DBA | Lizenz-Quellensteuer |
|---|---|
| DE-USA | 0 % (Art. 12 DBA-USA bei Antragsverfahren) |
| DE-CH | 0 % (Art. 12 DBA-CH) |
| DE-UK | 0 % (Art. 12 DBA-UK) |
| DE-FR | 0 % (EU-Zinsen-Lizenz-RL 2003/49/EG bei Konzernschwester) |
| DE-NL | 0 % (Art. 12 DBA-NL) |
| DE-China | 10 % |
| DE-Indien | 10 % |

→ Vor Vertragsschluss: DBA pruefen, Freistellungsbescheinigung beantragen.

### C. EU-Zinsen-Lizenzgebuehren-Richtlinie (2003/49/EG)

Bei Lizenzen zwischen verbundenen Unternehmen (mindestens 25 % Beteiligung) in EU-Mitgliedstaaten: Quellensteuer 0 %.

### D. Umsatzsteuer

- B2B Lizenz innerhalb EU: Reverse-Charge ($ 13b UStG)
- B2C Lizenz: USt-Pflicht im Empfaengerland
- Aussergewoehnliche Geschaeftsveraeusserung im Ganzen: $ 1 Ia UStG - bei IP-Voll-Uebertragung ggf. einschlaegig (siehe EuGH Zita Modes C-497/01)

## Klausel-Bausteine

**A. Quellensteuer-Klausel (Gross-up):**
> "$ 19 Steuern.
> (1) Lizenzgebuehren sind ohne Abzug von Steuern, Gebuehren oder anderen Abgaben zu zahlen.
> (2) Sofern der Lizenznehmer kraft Gesetzes verpflichtet ist, von der Lizenzgebuehr Quellensteuer einzubehalten, erhoeht sich die Lizenzgebuehr um den Betrag der Quellensteuer (Gross-up), so dass der Lizenzgeber den vertraglich vereinbarten Nettobetrag erhaelt.
> (3) Sofern der Lizenzgeber durch DBA-Anwendung oder die EU-Zinsen-Lizenz-Richtlinie einen reduzierten Quellensteuersatz oder Steuerbefreiung beanspruchen kann, wirkt er bei der Beschaffung der erforderlichen Bescheinigungen mit."

**B. Umsatzsteuer:**
> "(4) Die Lizenzgebuehren sind Nettobetraege. Auf die Lizenzgebuehr ist die gesetzliche Umsatzsteuer hinzuzurechnen. Bei B2B-Konstellationen innerhalb der EU gilt das Reverse-Charge-Verfahren ($ 13b UStG)."

**C. Steuer-Erstattung:**
> "(5) Wird die Quellensteuer rueckwirkend reduziert oder erstattet, fliesst der Erstattungsbetrag dem Lizenzgeber zu, soweit dieser den Gross-up bereits getragen hat."

## Pruefroutine vor Vertragsschluss

```
1. Ist der Lizenzgeber beschraenkt steuerpflichtig (Sitz im Ausland)?
2. Welches DBA gilt?
3. Quellensteuer-Reduktion moeglich?
4. Freistellungsbescheinigung BZSt vorhanden?
5. Gross-up-Klausel im Vertrag?
6. Verbundene Unternehmen? Dann EU-Zinsen-Lizenz-RL pruefen.
7. USt-Behandlung in Anlage E festhalten.
```

## Anschluss

- Verguetungsstruktur: `klausel-verguetung-pauschale-royalty-tiered`
- Rechtswahl bei Cross-Border: `klausel-rechtswahl-gerichtsstand-schiedsklausel`

---

## Skill: `lizenz-marke-markeng`

_Markenrechtslizenzen nach MarkenG $ 30: Qualitaetskontrolle, Bezeichnungspflicht, Eintragungspflicht im DPMA-Register $ 30 III, Erloeschen nicht-genutzter Marken $ 26, EU-Marken EUIPO. Mit Klauselbausteinen Qualitaetskontrolle._

# Lizenz Marke (MarkenG)

## Normenanker

- $ 27 MarkenG - Uebertragung der Marke (Voll-Verkauf)
- $ 30 MarkenG - Lizenz an der Marke (Teil-Recht)
- $ 30 Abs. 3 MarkenG - Eintragung der Lizenz im DPMA-Register (Dritt-Wirkung)
- $ 14 MarkenG - Ausschlussrecht (Verletzungen)
- $ 26 MarkenG - Benutzungspflicht (5 Jahre); Loeschung mangels Benutzung
- $ 33 ff. MarkenG - Anmeldung, Eintragung, Loeschung
- UMV (EU) 2017/1001 - Unionsmarke EUIPO

## Lizenzformen

| Typ | Definition |
|---|---|
| ausschliessliche Lizenz | nur Lizenznehmer + Lizenzgeber selbst; kann weiter beschraenkt sein |
| einfache Lizenz | weitere Lizenzen moeglich |
| raeumlich beschraenkt | EU-Mitgliedstaat / Region |
| sachlich beschraenkt | Waren-/Dienstleistungsklassen (Nizzaer Klassifikation) |
| zeitlich beschraenkt | konkrete Laufzeit |

## Qualitaetskontrolle als Pflichtbaustein

Anders als Patent/Urheberrecht ist die **Qualitaetskontrolle** bei Markenlizenz dogmatischer Pflichtbaustein:

- Marke garantiert konstante Qualitaet; ohne Qualitaetskontrolle Lizenz nichtig (Tachenbuch) oder Marke verfaellt.
- Klausel: Lizenzgeber hat **Mitspracherecht** bei Produktqualitaet, Verpackung, Werbung, Vertriebskanaelen.
- Pruefintervall: jaehrlich; Pruefberichts-Aufnahme.

## Benutzungspflicht $ 26 MarkenG

- Lizenznehmer-Benutzung gilt als Benutzung der Marke $ 26 Abs. 2 MarkenG.
- → Vertraglich Mindestbenutzung sichern, sonst Loeschungsantrag durch Dritte.

## Eintragung im DPMA-Register

- $ 30 Abs. 3 MarkenG: Eintragung der Lizenz hat **deklaratorischen Charakter**, aber wichtige Dritt-Wirkung (Sukzessionsschutz).
- Antrag durch beide Parteien; Kosten regelmaessig Lizenznehmer.

## Klausel-Bausteine (DE)

**1. Lizenzgegenstand Marke:**
> "Der Lizenzgeber raeumt dem Lizenznehmer hiermit das [einfache / ausschliessliche] Recht ein, die in **Anlage A** aufgefuehrte(n) Marke(n) ("Lizenzmarken") fuer die in **Anlage B** definierten Waren und Dienstleistungen im Sinne der Nizzaer Klassifikation in [Territorium] zu nutzen."

**2. Qualitaetskontrolle:**
> "Der Lizenznehmer verpflichtet sich, die Lizenzmarken nur in einer Qualitaet zu nutzen, die der vom Lizenzgeber vorgegebenen Markenfuehrungsrichtlinie ("Brand Guideline") entspricht. Der Lizenzgeber hat ein Pruefrecht hinsichtlich Produktqualitaet, Verpackung und Werbeauftritt."

**3. Benutzungspflicht:**
> "Der Lizenznehmer wird die Lizenzmarken bestimmungsgemaess und in markenrechtlich erforderlicher Weise nutzen. Bei dauerhafter Nichtbenutzung von mehr als drei zusammenhaengenden Jahren ist der Lizenzgeber zur ausserordentlichen Kuendigung berechtigt."

**4. Eintragung:**
> "Die Parteien beantragen die Eintragung der Lizenz im Markenregister nach $ 30 Abs. 3 MarkenG. Die Eintragungsgebuehren traegt der Lizenznehmer."

## Anschluss

- Verguetung: `klausel-verguetung-pauschale-royalty-tiered`
- Verbesserungen / Markenfortentwicklung: `klausel-verbesserungen-grant-back`
- Eintragung Co-Branding: nur einzelfallweise sinnvoll

---

## Skill: `output-vertrag-englisch-fertigentwurf`

_Output: vollstaendiger Lizenzvertrag in englischer Sprache (Licence Agreement). Standard-Klauseln in English Law / German-Law-Variante; Royalty / Sublicensing / Indemnification / Governing Law / Arbitration. Bilingual-faehig._

# Output: Licence Agreement in English

## When to use English

- International deal with non-German party
- Governing law not German (e.g., English, NY, Swiss)
- Arbitration in English-speaking forum
- Parent-company headquartered abroad

## Standard Structure (mirrors the German version)

```
LICENCE AGREEMENT

between

[Licensor], [address], represented by [representative]
- the "Licensor" -

and

[Licensee], [address], represented by [representative]
- the "Licensee" -

- collectively the "Parties" -

PREAMBLE

(A) The Licensor [is the sole/joint] owner of the [patents, trademarks,
    designs, software, know-how] listed in Annex A.
(B) The Licensee wishes to obtain a licence for [purpose].
(C) The Parties have entered into a non-disclosure agreement dated [date]
    and have conducted due diligence.

The Parties agree as follows:

Sec. 1   Definitions
Sec. 2   Licensed IP
Sec. 3   Scope of Licence (Territory, Time, Field of Use)
Sec. 4   Exclusivity (sole / exclusive / non-exclusive)
Sec. 5   Royalties
Sec. 6   Sub-Licences
Sec. 7   Improvements / Grant-Back
Sec. 8   Representations and Warranties
Sec. 9   Limitation of Liability
Sec. 10  Reporting, Audit, Minimum Royalty
Sec. 11  Term and Termination
Sec. 12  Consequences of Termination
Sec. 13  Confidentiality
Sec. 14  Source-Code Escrow (if software)
Sec. 15  Governing Law and Dispute Resolution
Sec. 16  Insolvency Provisions
Sec. 17  Export Control
Sec. 18  Data Protection
Sec. 19  Taxes
Sec. 20  Miscellaneous

[Place], [date]

___________________________     ___________________________
Licensor                          Licensee

ANNEXES
Annex A — Licensed IP
Annex B — Field of Use
Annex C — Royalty Schedule + Reporting
Annex D — Data Processing Agreement (GDPR)
Annex E — Sub-Licensee List
```

## Key Clauses (English)

**Sec. 2 — Licensed IP:**
> "Licensor hereby grants Licensee a [non-exclusive / sole / exclusive] licence to use the intellectual property rights listed in Annex A (the 'Licensed IP') for the Field of Use defined in Annex B in the Territory defined herein."

**Sec. 5 — Royalties:**
> "Licensee shall pay to Licensor a running royalty of [X] % of Net Sales of Licensed Products. 'Net Sales' means gross invoiced sales less customary discounts, returns, value-added tax and shipping costs. Royalties are payable within thirty (30) days after the end of each calendar quarter."

**Sec. 15 — Governing Law and Arbitration (English law, LCIA):**
> "This Agreement shall be governed by and construed in accordance with the laws of England and Wales. Any dispute arising out of or in connection with this Agreement, including any question regarding its existence, validity or termination, shall be referred to and finally resolved by arbitration under the LCIA Rules. The seat of arbitration shall be London. The number of arbitrators shall be three. The language of the arbitration shall be English."

**Sec. 15 — Alternative (German law, DIS):**
> "This Agreement shall be governed by the laws of the Federal Republic of Germany under exclusion of the United Nations Convention on Contracts for the International Sale of Goods (CISG). Any dispute arising out of or in connection with this Agreement shall be finally settled under the DIS Arbitration Rules. The seat of arbitration shall be Frankfurt am Main. The language of arbitration shall be English."

## Anschluss

- German fassung: `output-vertrag-deutsch-fertigentwurf`
- Bilingual: `output-zweisprachig-bilingual-deutsch-englisch`

---

## Skill: `lizenz-geschaeftsgeheimnis-knowhow-geschgehg`

_Lizenz von Geschaeftsgeheimnissen und Know-how nach GeschGehG: $$ 1-12 GeschGehG; Schutzmassnahmen $ 2 Nr. 1b; Reverse Engineering $ 3; Sphaeren-Trennung; Know-how-Lizenz mit Vertraulichkeitsklauseln und Sanktionsregelungen._

# Lizenz Geschaeftsgeheimnis / Know-how (GeschGehG)

## Normenanker

- $ 1 GeschGehG - Schutzgegenstand
- $ 2 GeschGehG - Begriffsbestimmungen; $ 2 Nr. 1: Geschaeftsgeheimnis = vertrauliche Information mit Schutzmassnahmen und wirtschaftlichem Wert
- $ 3 GeschGehG - Erlaubte Handlungen (Reverse Engineering bei rechtmaessig erlangter Sache!)
- $ 4 GeschGehG - Verbotene Handlungen
- $ 5 GeschGehG - Schutzausnahmen (Whistleblowing, Journalistik, Aufdeckung Fehlverhalten)
- $$ 6-12 GeschGehG - Rechtsfolgen (Unterlassung, Schadensersatz, Auskunft, Vernichtung)

## Pflichtbaustein: Schutzmassnahmen vor Lizenz

Damit Know-how als Geschaeftsgeheimnis schutzfaehig bleibt, muss der Lizenzgeber vor Vertragsschluss nachweisen, dass:

1. **Zugriffsbeschraenkungen** - Need-to-Know, MFA, Branch Protection
2. **NDAs** mit Mitarbeitern, Beratern, Sub-Unternehmern
3. **Dokumentation** der Schutzmassnahmen
4. **Technische Sicherungen** (Verschluesselung, Audit-Trail)

Ohne Schutzmassnahmen kein Geheimnis, kein Schutz, keine durchsetzbare Lizenz.

## Reverse Engineering — Sonderfall

$ 3 GeschGehG: Reverse Engineering einer rechtmaessig erlangten Sache ist **erlaubt**, soweit der Inhaber das nicht vertraglich ausgeschlossen hat.

→ Im Lizenzvertrag: **Reverse-Engineering-Verbot** ausdruecklich vereinbaren ($ 3 Abs. 2 GeschGehG).

## Lizenztypen

| Typ | Inhalt |
|---|---|
| Know-how-Lizenz | Berechtigung zur Nutzung vertraulicher Informationen + Schulungspflicht des Lizenzgebers |
| Mixed Lizenz | Know-how + Patent + Marke kombiniert (TT-GVO-relevant) |
| NDA-Lizenz | reine Geheimhaltungsverpflichtung ohne Nutzungsrecht (selten - eher pre-License) |

## Klausel-Bausteine (DE)

**1. Lizenzgegenstand Geschaeftsgeheimnis:**
> "Der Lizenzgeber raeumt dem Lizenznehmer hiermit das nicht-ausschliessliche, nicht-uebertragbare Recht ein, das in **Anlage A** bezeichnete Know-how ("Lizenz-Know-how") fuer die in **Anlage B** definierten Zwecke zu nutzen. Das Lizenz-Know-how umfasst die in Anlage A aufgefuehrten technischen Unterlagen, Daten, Prozessbeschreibungen und Quellcode-Auszuege."

**2. Vertraulichkeitspflicht:**
> "Der Lizenznehmer verpflichtet sich, das Lizenz-Know-how mit der Sorgfalt eines ordentlichen Kaufmanns geheim zu halten. Insbesondere wird der Lizenznehmer (i) Zugriff auf das Need-to-Know-Prinzip beschraenken, (ii) Mitarbeitern und Beratern entsprechende Geheimhaltungsvereinbarungen auferlegen, (iii) das Lizenz-Know-how durch technische Massnahmen sichern und (iv) keine Kopien ausserhalb des Vertragsbereichs anfertigen."

**3. Reverse-Engineering-Verbot:**
> "Der Lizenznehmer wird das Lizenz-Know-how nicht reverse-engineeren, dekompilieren oder durch Analyse der Erscheinungsform Rueckschluesse auf seine Bestandteile ziehen. Dieses Verbot gilt im Sinne des $ 3 Abs. 2 GeschGehG."

**4. Rueckgabepflicht:**
> "Nach Vertragsbeendigung gibt der Lizenznehmer saemtliche schriftlichen und elektronischen Unterlagen des Lizenz-Know-hows binnen 30 Tagen zurueck oder vernichtet sie nachweislich; bestaetigt schriftlich gegenueber dem Lizenzgeber."

## Anschluss

- NDA fuer Vorvertrag: `klausel-vertraulichkeit-und-nda-interimsphase` (folgt)
- Insolvenz: `insolvenz-fortbestand-paragraf-103-inso-lizenz`

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

