---
name: kaltstart-interview
description: >
  Ersteinrichtungs-Interview für das gesellschaftsrechtliche Praxisprofil — erfasst
  Tätigkeitsbereiche (M&A, Gesellschafterversammlung/Aufsichtsrat, Kapitalmarkt,
  Gesellschaftsverwaltung), Wesentlichkeitsschwellen, Hausstil und Eskalationsmatrix.
  Lädt, wenn CLAUDE.md noch [PLATZHALTER]-Marker enthält, bei Neumandat (--neues-mandat)
  oder zur Überprüfung von Integrationen (--integrationen-pruefen).
language: de
when_to_use: |
  Trigger phrases and example requests:
  - Ersteinrichtung
  - Praxisprofil einrichten
  - cold-start
  - Setup starten
  - Mandatsprofil anlegen
  - Konfiguration aktualisieren
  - neues Mandat
  - Integrationen prüfen
  - Profil neu aufsetzen
argument-hint: "[--redo | --neues-mandat | --integrationen-pruefen | --modul [ma | aufsichtsrat | kapitalmarkt | gesellschaften]]"
---

# Ersteinrichtungs-Interview

## Zweck

Gesellschaftsrechtliche Mandate variieren erheblich: Ein GmbH-Syndikusrechtsanwalt (§ 46 BRAO) bei einem Start-up führt M&A-Transaktionen durch, pflegt die Gesellschafterliste und protokolliert Gesellschafterbeschlüsse. Ein Kanzleianwalt bei einem DAX-Konzern verantwortet möglicherweise nur BaFin-Meldepflichten oder die Vorbereitung von Hauptversammlungen. Dieses Interview ermittelt, welche Bereiche für den Nutzer aktiv sind, und baut ausschließlich das relevante Praxisprofil — keine leeren Abschnitte für nicht anwendbare Bereiche.

Beim Aufruf mit `--integrationen-pruefen`: Nur Teil 0 „Was ist verbunden?" neu ausführen und die `## Verfügbare Integrationen`-Tabelle in CLAUDE.md aktualisieren. Integration nur als ✓ ausweisen, wenn ein MCP-Tool-Aufruf tatsächlich erfolgreich war.

## Eingaben

- Angaben des Nutzers zu Tätigkeit, Kanzlei-/Unternehmensprofil und aktivem Modul
- Optional: Bestehende Zuständigkeits- und Vollmachtsmatrix, Organisationsstruktur, Gesellschafterliste
- Seed-Dokumente je Modul (Due-Diligence-Anforderungsliste, Muster-Problemvermerk, Muster-Beschlüsse)
- Integrationsstatus (Datenraum, Boardportal, Dokumentenablage)

## Rechtlicher Rahmen

Die nachfolgenden Vorschriften bilden den rechtlichen Rahmen der unterstützten Tätigkeitsbereiche:

**Gesellschaftsrecht allgemein:** §§ 1 ff. GmbHG; §§ 1 ff. AktG; §§ 105 ff. HGB (OHG), §§ 161 ff. HGB (KG); §§ 705 ff. BGB n.F. (GbR seit 01.01.2024, MoPeG); §§ 1 ff. UmwG (Verschmelzung, Spaltung, Formwechsel).

**M&A / Unternehmenskauf:** § 311 AktG (faktischer Konzern); § 15 GmbHG (Abtretung von Geschäftsanteilen, notarielle Form); § 17 GmbHG (Kaduzierung); §§ 29 ff. GmbHG (Jahresabschluss, Gewinnverwendung). Für Beteiligungserwerb an AGs: WpÜG (Pflichtangebot ab 30 % Stimmrechte, § 29 WpÜG); §§ 327a ff. AktG (Squeeze-out).

**Beschlussfassung / Governance:** § 48 GmbHG (Gesellschafterversammlung; Abs. 2: schriftliche Abstimmung ohne Versammlung); § 49 GmbHG (Einberufung); §§ 118 ff. AktG (Hauptversammlung; § 130 AktG: Niederschrift durch Notar bei AG); §§ 95 ff. AktG (Aufsichtsrat); § 23 Abs. 5 AktG (Satzungsstrenge).

**Mitbestimmung:** MitbestG (Unternehmen > 2.000 Arbeitnehmer); DrittelbG (Unternehmen 500–2.000 Arbeitnehmer); § 76 AktG (Vorstand); BetrVG (betriebliche Mitbestimmung). BGH, Urt. v. 23.09.2014 – II ZR 44/13, NZG 2014, 1332 (Beschlussmängelrecht GmbH, analoge Anwendung der §§ 241 ff. AktG). BGH, Urt. v. 29.01.2020 – II ZR 417/18, NJW 2020, 1804 (Treuepflicht im GmbH-Gesellschafterverhältnis).

**Kommentarliteratur:** Lutter/Hommelhoff/Bayer, GmbHG, 21. Aufl. 2023, § 48 Rn. 1 ff. (schriftliche Abstimmung); Hüffer/Koch, AktG, 16. Aufl. 2024, § 130 Rn. 1 ff. (Niederschrift HV); MüKoAktG/Kubis, 5. Aufl. 2022, § 130 Rn. 5 ff.; Scholz/Priester, GmbHG, 13. Aufl. 2022, § 48 Rn. 20 ff.

## Ablauf

### Schritt 0: Bestandsaufnahme

CLAUDE.md lesen:
- **Nicht vorhanden** → Interview starten.
- **Enthält `<!-- EINRICHTUNG PAUSIERT BEI: -->`** → Nutzer begrüßen, Fortsetzung anbieten.
- **Enthält `[PLATZHALTER]`, aber keinen Pause-Kommentar** → Vorlage unvollständig; Neustart oder Fortsetzen anbieten.
- **Vollständig befüllt** → bereits konfiguriert; überspringen, außer bei `--redo` oder `--modul [name]`.

**Modul-Flags:**
- `--redo` — vollständiges Re-Interview, überschreibt alle Abschnitte
- `--modul [ma | aufsichtsrat | kapitalmarkt | gesellschaften]` — einzelnes Modul hinzufügen oder aktualisieren
- `--neues-mandat` — Haus-Einrichtung überspringen, direkt zum transaktionsspezifischen Kontext (nur M&A-Modul)

### Schritt 0.5: Vorspann und Modulauswahl (1–2 Min.)

Vor allen weiteren Fragen zeigen:

> **`gesellschaftsrecht` unterstützt M&A-Transaktionen, Beschlussfassung und gesellschaftsrechtliche Governance, Kapitalmarktrecht sowie Gesellschaftsverwaltung und Compliance.** Anderer Schwerpunkt? Wenden Sie sich an den Legal-Builder-Hub.
>
> **2 Minuten** für Rolle, Tätigkeitssetting, Zuständigkeitsbereich und Modulauswahl. **15 Minuten** für Wesentlichkeitsschwellen im Vertragsreview, Hausstil für Beschlüsse, Gesellschafterlisten und Eskalationsmatrix.
>
> Kurzversion oder vollständige Einrichtung?

Dann fragen, welche Module aktiv sind:

> 1. **M&A** — Unternehmenskäufe, -verkäufe, Beteiligungserwerb, Fusionen
> 2. **Governance / Beschlussfassung** — Vorbereitung von Gesellschafterversammlungen, Aufsichtsratssitzungen, Protokollen, Beschlüssen
> 3. **Kapitalmarkt** — BaFin-Meldepflichten, WpHG-Compliance, Hauptversammlung börsennotierter AG, Ad-hoc-Publizität
> 4. **Gesellschaftsverwaltung** — Tochtergesellschaften, Gesellschafterliste, Jahresabschluss, Handelsregisterpflichten

### Schritt 1: Unternehmensprofil (immer, 2 Min.)

- Name der Kanzlei / des Unternehmens (für Arbeitsergebnis-Kopfzeilen)
- Tätigkeitssetting: Sozietät (solo/klein/groß) | Syndikusrechtsanwalt in-house | Behörde/Rechtsamt
- Branche und Rechtsform des betreuten Unternehmens (GmbH / AG / KG / GbR / SE)
- Eingetragener Sitz und relevante Handelsregister (HRB/HRA-Nummer)
- Größe des Rechtsteams
- Eskalationsmatrix: Wer entscheidet bei wesentlichen Fragen — Geschäftsführung, Aufsichtsrat, externer Anwalt?

Falls kein Vollmachts- und Zuständigkeitsdokument hochgeladen: Angebot, eine kompakte Vollmachtsmatrix als Standalone-Dokument zu erstellen.

### Schritt 2M: M&A-Modul (4–6 Min., falls aktiv)

- Käufer- oder Verkäuferseite als Regelfall?
- Serienakquisiteur mit Standard-Playbook oder transaktionsspezifisch?
- Wer leitet Transaktionen: Corporate-Development-Abteilung, Rechtsabteilung, externe Kanzlei als Federführer?
- Wesentlichkeitsschwelle für Vertragsreview (alle Verträge? Ab X EUR? Top-N-Verträge nach Umsatz?)
- Genutzter VDR: Intralinks, Datasite, Datenraum-eigener Cloud-Speicher?
- Seed-Dokumente: Due-Diligence-Anforderungsliste und ein früherer Problemvermerk (abgeschlossenes Mandat)

Aus Seed-Dokumenten extrahieren: Kategorienstruktur, Schwellenwerte, Hausformat für Problemvermerke.

### Schritt 2G: Governance/Beschlussfassung-Modul (3–4 Min., falls aktiv)

- Funktion: Geschäftsführer, Prokurist, Syndikusrechtsanwalt, externer Berater?
- Größe und Zusammensetzung des Aufsichtsrats / Beirats (falls vorhanden)
- Welche Form von Beschlüssen überwiegt: Gesellschafterbeschlüsse (§ 48 GmbHG), Aufsichtsratsbeschlüsse, Vorstandsbeschlüsse?
- Routinemäßige Nutzung des schriftlichen Verfahrens (§ 48 Abs. 2 GmbHG)? Bei welchen Gegenständen?
- Muster-Protokolle und Musterbeschlüsse hochladen (abgeschlossene Verfahren)

Bei AG zusätzlich: Hauptversammlung (Präsenz, virtuelle HV nach § 118a AktG, hybride HV); Notarielle Niederschrift (§ 130 AktG) — wer beauftragt den Notar?

### Schritt 2K: Kapitalmarkt-Modul (3–4 Min., falls aktiv)

- Börsenplatz (XETRA/Frankfurt, m:access, SDAX/MDAX/DAX, Drittbörse)?
- Geschäftsjahresende und Berichtspflichten (HGB oder IFRS)?
- BaFin-Meldepflichten: Stimmrechtsmitteilungen (§§ 33 ff. WpHG), Insiderverzeichnis (Art. 18 MAR)?
- Offenlegungsausschuss: Zusammensetzung, Turnus?
- Zuständigkeit für Ad-hoc-Publizität (Art. 17 MAR) — Rechtsabteilung, IR, Vorstand?

### Schritt 2V: Gesellschaftsverwaltungs-Modul (2–3 Min., falls aktiv)

- Anzahl aktiv verwalteter Gesellschaften
- Wesentliche Sitzstaaten (Deutschland, EU, Drittstaaten)
- Registerführung: Elektronische Gesellschafterliste (§ 40 GmbHG), automatische Handelsregisterüberwachung?
- Nutzung eines Entity-Management-Systems oder Tabellenkalkulation?
- Jahresabschluss-Pflichten (§§ 242 ff. HGB; Offenlegung §§ 325 ff. HGB)?

### Nach dem Interview

Zusammenfassung zeigen, Praxisprofil erstellen, Pflege erläutern:

> Ihr Praxisprofil liegt in CLAUDE.md. Änderungen jederzeit direkt oder per `/gesellschaftsrecht:kaltstart-interview --redo` möglich. Am häufigsten angepasst: Wesentlichkeitsschwellen, Hausstil für Beschlüsse, Eskalationsmatrix.

## Ausgabeformat

- Praxisprofil in CLAUDE.md mit allen aktiven Modulen und befüllten Abschnitten
- Keine `[PLATZHALTER]` in abgeschlossenen Sektionen — nur bewusst ausgelassene Felder als `[AUSSTEHEND]` markieren
- Tabellarische Übersicht aktiver Module mit Kurzbeschreibung

## Beispiel

**Szenario:** Syndikusrechtsanwalt einer GmbH mit 200 Mitarbeitern, aktive Module M&A und Governance.

Nach dem Interview: Praxisprofil enthält Wesentlichkeitsschwelle 100.000 EUR für Vertragsreview, Hausstil „BESCHLOSSEN:" für schriftliche Gesellschafterbeschlüsse nach § 48 Abs. 2 GmbHG, Eskalation zu externem M&A-Berater ab Transaktionsvolumen > 5 Mio. EUR. Kapitalmarkt- und Gesellschaftsverwaltungsmodul: nicht aktiviert.

## Risiken und typische Fehler

- **Alle Module als aktiv annehmen.** Erst fragen, dann nur relevante Abschnitte aufbauen. Ein M&A-Anwalt braucht kein Kapitalmarkt-Modul.
- **Käuferseite als Regelfall annehmen.** Das Praxisprofil erfasst den Hausstandard; die spezifische Rolle je Transaktion wird mit `--neues-mandat` festgelegt.
- **Generische Platzhalter eintragen.** „Übliche Wesentlichkeitsschwellen" ist kein Schwellenwert. Nach konkreten Zahlen fragen.
- **Seed-Dokumente für inaktive Module anfordern.** Nur die Anforderungsliste und den Problemvermerk anfordern, wenn M&A aktiv ist.
- **Faktenprüfung unterlassen.** Wenn der Nutzer eine Norm oder Frist nennt (z.B. „Anmeldefrist 3 Wochen nach Beschluss"), plausibilisieren und bei Abweichung flaggen: „[Prämisse geprüft — bitte verifizieren]".

## Quellenpflicht

Jeder Verweis auf Vorschriften in CLAUDE.md und in Skill-Ausgaben muss zitieren:
- Gesetze mit Paragraphenzeichen: `§ 48 Abs. 2 GmbHG`, `§ 130 AktG`
- BGH-Entscheidungen in voller Zitierung: `BGH, Urt. v. 23.09.2014 – II ZR 44/13, NZG 2014, 1332`
- Kommentare im Bearbeiterstil: `Lutter/Hommelhoff/Bayer, GmbHG, 21. Aufl. 2023, § 48 Rn. 5`
- Keine bloßen Gesetzesnummern ohne Paragraphenzeichen

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
