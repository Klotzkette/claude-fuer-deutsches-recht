---
name: gesellschaftsrecht-kaltstart-interview
description: "Ersteinrichtungs-Interview für das gesellschaftsrechtliche Praxisprofil — erfasst Tätigkeitsbereiche (M&A, Gesellschafterversammlung/Aufsichtsrat, Kapitalmarkt, Gesellschaftsverwaltung), Wesentlichkeitsschwellen, Hausstil und Eskalationsmatrix. Lädt, wenn CLAUDE.md noch [PLATZHALTER]-Marker enthält, bei Neumandat (--neues-mandat) oder zur Überprüfung von Integrationen (--integrationen-prüfen)."
---

# Ersteinrichtungs-Interview

## Triage zu Beginn

Vor dem Kaltstart-Interview klaeren:

1. **Profil bereits vorhanden?** CLAUDE.md lesen: vollstaendig befuellt? Falls ja: `--redo` oder `--modul [name]` verwenden, kein Neustart.
2. **Aufruf-Flag?** `--neues-mandat` (nur Transaktionskontext), `--modul ma/aufsichtsrat/kapitalmarkt/gesellschaften` (nur ein Modul), `--integrationen-pruefen` (nur Integrationen), `--redo` (Vollneustart).
3. **Zeitbudget des Nutzers?** 2 Minuten (Kurzversion: nur Rolle + aktive Module) oder 15 Minuten (vollstaendige Einrichtung inkl. Schwellenwerte und Hausstil)?
4. **Welche Module werden benoetigt?** Nicht alle Module annehmen; Nutzer explizit fragen. Pro-Tipp: Die meisten Nutzer brauchen 1-2 Module, nicht alle vier.
5. **Seed-Dokumente verfuegbar?** Wenn Nutzer Due-Diligence-Anforderungsliste oder Musterbeschluesse hochgeladen hat: aus diesen extrahieren statt manuell fragen.

## Zweck

Gesellschaftsrechtliche Mandate variieren erheblich: Ein GmbH-Syndikusrechtsanwalt (§ 46 BRAO) bei einem Start-up führt M&A-Transaktionen durch, pflegt die Gesellschafterliste und protokolliert Gesellschafterbeschlüsse. Ein Kanzleianwalt bei einem DAX-Konzern verantwortet möglicherweise nur BaFin-Meldepflichten oder die Vorbereitung von Hauptversammlungen. Dieses Interview ermittelt, welche Bereiche für den Nutzer aktiv sind, und baut ausschließlich das relevante Praxisprofil — keine leeren Abschnitte für nicht anwendbare Bereiche.

Beim Aufruf mit `--integrationen-prüfen`: Nur Teil 0 "Was ist verbunden?" neu ausführen und die `## Verfügbare Integrationen`-Tabelle in CLAUDE.md aktualisieren. Integration nur als ✓ ausweisen, wenn ein MCP-Tool-Aufruf tatsächlich erfolgreich war.

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

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

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

> Ihr Praxisprofil liegt in CLAUDE.md. Änderungen jederzeit direkt oder per `/gesellschaftsrecht:gesellschaftsrecht-kaltstart-interview --redo` möglich. Am häufigsten angepasst: Wesentlichkeitsschwellen, Hausstil für Beschlüsse, Eskalationsmatrix.

## Ausgabeformat

- Praxisprofil in CLAUDE.md mit allen aktiven Modulen und befuellten Abschnitten
- Keine `[PLATZHALTER]` in abgeschlossenen Sektionen — nur bewusst ausgelassene Felder als `[AUSSTEHEND]` markieren
- Tabellarische Uebersicht aktiver Module mit Kurzbeschreibung

## Output-Template

**Adressat:** Praxis-Nutzer / Kanzlei-intern — Tonfall: sachlich-bestaedigend, handlungsanleitend

```
## Gesellschaftsrecht Praxisprofil
_Erstellt: [TT.MM.JJJJ] — Version 1.0_

### Unternehmen / Kanzlei
Name: [KANZLEI / UNTERNEHMEN]
Taetigkeitssetting: [Sozietaet / Syndikusrechtsanwalt in-house / Rechtsamt]
Branche: [BRANCHE]
Rechtsform betreuter Gesellschaften: [GmbH / AG / SE / KG / etc.]
Sitz: [ORT]
Registergericht: [AMTSGERICHT ORT] — HRB [NUMMER]
Rechtsteam-Groesse: [N] Personen

### Eskalationsmatrix
Wesentliche Entscheidungen: [PERSON / GREMIUM]
Externe Eskalation ab: [BETRAG EUR / BESCHREIBUNG]
Externe Kanzlei: [NAME]

### Aktive Module
| Modul | Aktiv | Konfiguriert |
|---|---|---|
| M&A | [JA / NEIN] | [JA / AUSSTEHEND] |
| Governance / Beschlussfassung | [JA / NEIN] | [JA / AUSSTEHEND] |
| Kapitalmarkt | [JA / NEIN] | [JA / AUSSTEHEND] |
| Gesellschaftsverwaltung | [JA / NEIN] | [JA / AUSSTEHEND] |

### M&A-Modul (falls aktiv)
Regelfall: [Kaeuferseite / Verkaeuferseite / variabel]
Wesentlichkeitsschwelle Vertragsreview: [BETRAG EUR]
VDR-Plattform: [INTRALINKS / DATASITE / ANDERES]
KI-Massenreview-Vertrauen: [ERGEBNIS UEBERNEHMEN / 10-PROZENT-STICHPROBE / VOLLPRUEFUNG]

### Governance-Modul (falls aktiv)
Hausbeschlussformat: [BESCHLOSSEN: / Beschluss Nr. / etc.]
Bevorzugte Unterzeichner: [LISTE]
Notarielle Beurkundung erforderlich bei: [SATZUNGSAENDERUNG / KAPITALMASNAHME / etc.]

### Gesellschaftsverwaltungs-Modul (falls aktiv)
Anzahl aktiv verwalteter Gesellschaften: [N]
Entity-Management-System: [NAME / TABELLE]
Jahresabschluss-Pflichten: [HGB / IFRS]

### Integrationen
| System | Status | Letzter Test |
|---|---|---|
| [VDR-NAME] | [VERBUNDEN / NICHT VERBUNDEN] | [DATUM] |
| Handelsregister | [VERBUNDEN / NICHT VERBUNDEN] | [DATUM] |

_Profil-Pflege: Einzelne Aenderungen per `/gesellschaftsrecht:gesellschaftsrecht-anpassen`.
Vollstaendige Neueinrichtung per `/gesellschaftsrecht:gesellschaftsrecht-kaltstart-interview --redo`._
```

## Rote Schwellen

- **Modul-Annahme ohne Nachfragen** — nicht alle Module als aktiv annehmen; Nutzer verliert Zeit mit irrelevanten Fragen; immer zuerst fragen.
- **Konkrete Schwellenwerte nicht erfasst** — 'uebliche Schwellen' ist kein Wert; nach Zahlen fragen.
- **Profil mit Platzhaltern abgeschlossen** — `[PLATZHALTER]` in CLAUDE.md fuehrt dazu, dass Skills falsche Defaultwerte verwenden; nur als `[AUSSTEHEND]` mit Erklaerung belassen.

## Beispiel

**Szenario:** Syndikusrechtsanwalt einer GmbH mit 200 Mitarbeitern, aktive Module M&A und Governance.

Nach dem Interview: Praxisprofil enthält Wesentlichkeitsschwelle 100.000 EUR für Vertragsreview, Hausstil "BESCHLOSSEN:" für schriftliche Gesellschafterbeschlüsse nach § 48 Abs. 2 GmbHG, Eskalation zu externem M&A-Berater ab Transaktionsvolumen > 5 Mio. EUR. Kapitalmarkt- und Gesellschaftsverwaltungsmodul: nicht aktiviert.

## Risiken und typische Fehler

- **Alle Module als aktiv annehmen.** Erst fragen, dann nur relevante Abschnitte aufbauen. Ein M&A-Anwalt braucht kein Kapitalmarkt-Modul.
- **Käuferseite als Regelfall annehmen.** Das Praxisprofil erfasst den Hausstandard; die spezifische Rolle je Transaktion wird mit `--neues-mandat` festgelegt.
- **Generische Platzhalter eintragen.** "Übliche Wesentlichkeitsschwellen" ist kein Schwellenwert. Nach konkreten Zahlen fragen.
- **Seed-Dokumente für inaktive Module anfordern.** Nur die Anforderungsliste und den Problemvermerk anfordern, wenn M&A aktiv ist.
- **Faktenprüfung unterlassen.** Wenn der Nutzer eine Norm oder Frist nennt (z.B. "Anmeldefrist 3 Wochen nach Beschluss"), plausibilisieren und bei Abweichung flaggen: "[Prämisse geprüft — bitte verifizieren]".

## Quellenpflicht

Jeder Verweis auf Vorschriften in CLAUDE.md und in Skill-Ausgaben muss zitieren:
- Gesetze mit Paragraphenzeichen: `§ 48 Abs. 2 GmbHG`, `§ 130 AktG`
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Keine bloßen Gesetzesnummern ohne Paragraphenzeichen

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
