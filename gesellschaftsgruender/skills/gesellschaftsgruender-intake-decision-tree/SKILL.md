---
name: gesellschaftsgruender-intake-decision-tree
description: "Decision Tree fuer das Intake-Formular als Mermaid-Diagramm. Conditional Logic Knoten Verzweigungen Pflichtfelder Trigger-Events Validierung. Vom Rechtsformwahl ueber Class-Shares Sperrminoritaet Sozialversicherung Notar-Pflicht bis Streit-Eskalation. Mit Workflow-Engine-Hinweisen Bryter Josef Documate. Outlook-Export Fristen-Engine."
---

# Intake Decision Tree

## Zweck

Grafischer Decision Tree fuer den Gruender-Intake-Workflow. Zeigt die **conditional logic**: welche Folgefragen sich aus welcher Antwort ergeben, wann welche Skills getriggert werden, wann welche Pflichtdokumente erzeugt werden.

Implementiert in **Mermaid**-Notation (rendert in GitHub, GitLab, Notion, Obsidian, VSCode, BitBucket).

---

## 1) Gesamt-Workflow

```mermaid
flowchart TD
    Start([Mandant fragt Gruendung an]) --> Intake[Gruender-Intake-Formular]

    Intake --> Q1{Anzahl Gruender?}
    Q1 -->|1| Solo[Solo-Gruender-Pfad]
    Q1 -->|2-3| StandardPath[Standard-Pfad]
    Q1 -->|4+| ComplexPath[Komplex-Pfad mit SHA]

    Solo --> Q2a{Kapital verfuegbar?}
    Q2a -->|< 5.000 EUR| UG_Pfad[UG-Pfad]
    Q2a -->|5.000 - 25.000 EUR| Q2b{Investor geplant?}
    Q2a -->|>= 25.000 EUR| GmbH_Pfad[GmbH-Pfad]

    Q2b -->|Ja| GmbH_Pfad
    Q2b -->|Nein| UG_Empfehlung[UG empfohlen]

    StandardPath --> Q3{Investor in 12 Monaten?}
    Q3 -->|Ja| ClassShares_jetzt[Class-Shares schon bei Gruendung]
    Q3 -->|Nein| ClassShares_spaeter[Class-Shares spaeter einfuehren]
    Q3 -->|Unklar| GenehmigtesKapital_jetzt[Genehmigtes Kapital vorsehen]

    ComplexPath --> ClassShares_jetzt

    ClassShares_jetzt --> SHA_Modul[SHA-Modul triggern]
    ClassShares_spaeter --> Satzung_Modul[Satzung-Modul triggern]
    GenehmigtesKapital_jetzt --> Satzung_Modul

    SHA_Modul --> Vesting{Vesting fuer Gruender?}
    Vesting -->|Ja| VestingKlausel[Vesting-Klausel SHA]
    Vesting -->|Nein| Stoppschild_Vesting[Warnung: Bad-Leaver-Risiko]

    VestingKlausel --> StimmBindung[Stimmbindungs-Klausel SHA]
    StimmBindung --> Notar[Notar-Vorbereitung]
    Satzung_Modul --> Notar
    UG_Pfad --> Notar
    UG_Empfehlung --> Notar

    Notar --> SV_Check{GF-Sozialversicherung?}
    SV_Check -->|Solo-GF| SV_frei[SV-frei]
    SV_Check -->|Mehrheits-GF| SV_frei
    SV_Check -->|Minderheits-GF| SV_Sperrminoritaet{Echte Sperrminoritaet in Satzung?}

    SV_Sperrminoritaet -->|Ja in Satzung| SV_frei
    SV_Sperrminoritaet -->|Nur in SHA| SV_pflichtig_Warnung[WARNUNG: BSG-Linie - SHA-Stimmbindung reicht nicht]
    SV_Sperrminoritaet -->|Keine| SV_pflichtig[SV-pflichtig]

    SV_frei --> Statusfeststellung[Statusfeststellung Paragraf 7a SGB IV beantragen]
    SV_pflichtig_Warnung --> Statusfeststellung
    SV_pflichtig --> Statusfeststellung

    Statusfeststellung --> HR_Anmeldung[Handelsregister-Anmeldung]
    HR_Anmeldung --> Behoerden[Gewerbe Finanzamt IHK BG TraFinG]
    Behoerden --> Compliance[Erste 100 Tage GF-Pflichten]
    Compliance --> Ende([Operatives Geschaeft])
```

---

## 2) Detail-Diagramm: Class-Shares-Modul

```mermaid
flowchart TD
    Start([Class-Shares-Modul]) --> Q1{Anzahl Klassen?}
    Q1 -->|1 nur Common| Klasse1[Standard-Satzung]
    Q1 -->|2 Common + B| Klasse2[Series-A-Strukur]
    Q1 -->|3+ Common A B C| Klasse3[Multi-Class-Struktur]

    Klasse2 --> Q2{Investor-Schutz}
    Q2 -->|Liquidation Preference| LiqPref[Klausel 6 Liquidation Preference]
    Q2 -->|Anti-Dilution| AntiDil[Klausel 7 Anti-Dilution]
    Q2 -->|Veto-Rechte| Veto[Sondervetorechte]

    LiqPref --> Q3{Participating oder non-participating?}
    Q3 -->|non-participating| LiqPref_NP[Beste Praxis bei Tech-Startup]
    Q3 -->|participating| LiqPref_Warnung[WARNUNG bei Mittelmaessigem Exit Vorteil Investor erheblich]

    AntiDil --> Q4{Methode?}
    Q4 -->|Weighted Average broad-based| AntiDil_WA[Standard empfohlen]
    Q4 -->|Full Ratchet| AntiDil_FR[Aggressiv nur bei riskanten Investments]

    Veto --> Q5{Reichweite}
    Q5 -->|Spezifische Themen| Veto_OK[Klausel 2 Golden Share angepasst]
    Q5 -->|Alle Beschluesse| Veto_Sittenwidrig[WARNUNG Sittenwidrigkeit Paragraf 138 BGB]
```

---

## 3) Detail-Diagramm: SV-Status-Pruefung

```mermaid
flowchart TD
    Start([SV-Status-Pruefung]) --> Q1{Ist der GF zugleich Gesellschafter?}
    Q1 -->|Nein - Fremd-GF| Fremd[Fremd-GF]
    Q1 -->|Ja| Q2{Anteilshoehe?}

    Fremd --> SV_pflichtig[SV-pflichtig BSG Linie]

    Q2 -->|>= 50%| Mehrheit[Mehrheits-GF]
    Q2 -->|< 50%| Q3{Sperrminoritaet?}

    Mehrheit --> SV_frei[SV-frei BSG Linie]

    Q3 -->|Ja in Satzung| Q4{Sperrminoritaet umfassend?}
    Q3 -->|Nur in SHA-Stimmbindung| SV_pflichtig_SHA[SV-pflichtig BSG 11.11.2015]
    Q3 -->|Keine| SV_pflichtig

    Q4 -->|Ja| SV_frei
    Q4 -->|Nur teilweise| SV_pruefen[Im Einzelfall pruefen]

    SV_pflichtig --> Statusfeststellung[Paragraf 7a SGB IV beantragen]
    SV_pflichtig_SHA --> Statusfeststellung
    SV_pflichtig --> Statusfeststellung
    SV_frei --> Statusfeststellung
    SV_pruefen --> Statusfeststellung

    Statusfeststellung --> Lohnabrechnung[Lohnabrechnung entsprechend einrichten]
```

---

## 4) Detail-Diagramm: Streit-Eskalations-Pfad

```mermaid
flowchart TD
    Start([Streitiger Gesellschafterbeschluss]) --> Q1{Beschluss bereits gefasst?}
    Q1 -->|Nein| Pravention[Praevention: SHA-Stimmbindung pruefen Beirat anrufen]
    Q1 -->|Ja| Q2{Bei HR eingereicht?}

    Q2 -->|Nein| Q3{Eilbeduerftigkeit gegeben?}
    Q2 -->|Ja| Sofort_eA[Einstweilige Verfuegung LG + Anmeldungs-Sperre Registergericht binnen 48h]

    Q3 -->|Ja| Sofort_eA
    Q3 -->|Nein| Anfechtungsklage[Anfechtungsklage binnen 1 Monat]

    Sofort_eA --> Q4{Verfuegung erlassen?}
    Q4 -->|Ja| Hauptverfahren[Hauptverfahren Anfechtungsklage]
    Q4 -->|Nein| Q5{Beschwerde?}
    Q5 -->|Ja| OLG[OLG-Beschwerde]
    Q5 -->|Nein| Hauptverfahren

    Anfechtungsklage --> Hauptverfahren
    OLG --> Hauptverfahren

    Hauptverfahren --> Beirat[Schlichtungs-Pflicht Beirat einhalten]
    Beirat --> Q6{Beirat Vergleich vorgeschlagen?}
    Q6 -->|Ja| Q7{Annahme?}
    Q6 -->|Nein| Verfahren_weiter[LG entscheidet]

    Q7 -->|Ja| Vergleich[Vergleich Klagrueckname]
    Q7 -->|Nein| Verfahren_weiter

    Verfahren_weiter --> Urteil[Urteil + ggf. Berufung]
    Pravention --> Vergleich
```

---

## 5) Pflichtfeld-Knotenpunkte

### Knoten 1 — Stammdaten

**Pflichtfelder**:
- Anzahl Gruender
- Identitaet (Name, Geburtsdatum, Anschrift, Ausweis-Nummer)
- Familienstand (fuer § 1365 BGB-Pruefung)
- Minderjaehrigkeit (fuer §§ 1643, 1822 BGB)

**Validierung**:
- Personalausweis-Nummer-Pruefung
- Bei Minderjaehrigkeit: Trigger Familiengerichtsgenehmigung

### Knoten 2 — Anteilsverteilung

**Pflichtfelder**:
- Stammkapital absolut
- Anteilshoehen pro Gruender
- Klassen-Festlegung (Common / A / B / C)

**Validierung**:
- Summe = 100 %
- Mindesthoehen pro Klasse
- Pflicht-Hinweis: bei Investor-Roadmap Class-Shares vorsehen

### Knoten 3 — Firma und IP

**Pflichtfelder**:
- Wunsch-Firma
- Sitz
- Geschaeftsgegenstand

**Validierung-Trigger**:
- HR-Suche bundesweit
- IHK-Vorpruefung
- DPMA / EUIPO-Recherche
- Domain-Verfuegbarkeit
- Bei Kollision: Alternativ-Vorschlaege anbieten

### Knoten 4 — Geschaeftsfuehrung

**Pflichtfelder**:
- Anzahl GF
- Gesellschafter oder Fremd-GF
- Anteilshoehe (falls Gesellschafter-GF)
- Anstellungsvertrag-Eckdaten

**Trigger**:
- SV-Status-Pruefung
- Statusfeststellung Paragraf 7a SGB IV
- Geschaeftsfuehrervertrag-Generierung

### Knoten 5 — SHA und Vesting

**Pflichtfelder bei Multi-Gruender**:
- Vesting-Periode (Standard 48 Monate)
- Cliff (Standard 12 Monate)
- Bad-Leaver-Definition
- Drag/Tag-Schwellen

### Knoten 6 — Beirat

**Optional, aber empfohlen**:
- Beirat ja/nein
- Anzahl Mitglieder
- Schlichtungs-Funktion ja/nein

### Knoten 7 — Notar

**Trigger**:
- DiRUG online oder physisch?
- Termin-Buchung
- Unterlagen-Liste generieren
- Stammkapital-Einzahlung vorbereiten

### Knoten 8 — Behoerden-Pflichten

**Trigger automatisch nach HR-Eintragung**:
- Gewerbeanmeldung
- ELSTER-Fragebogen
- IHK
- BG (Frist 1 Woche)
- TraFinG (unverzueglich)

---

## 6) Trigger-Events fuer Fristen-Engine

| Event | Frist | Aktion |
|---|---|---|
| HR-Eintragung | + 1 Woche | BG-Anmeldung erinnern |
| HR-Eintragung | + 1 Monat | ELSTER-Fragebogen einreichen |
| HR-Eintragung | + sofort | TraFinG-Meldung |
| Geschaeftsjahresende | + 3 Monate | Jahresabschluss aufstellen |
| Jahresabschluss | + 12 Monate | Bundesanzeiger-Veroeffentlichung |
| GV-Beschluss Kapitalerhoehung | + 1 Monat | Anfechtungsfrist abgelaufen |
| Krisenfrueherkennung-Trigger | + sofort | StaRUG-Pruefung oder § 49 III GmbHG-Versammlung |
| Insolvenz-Reife | + 3 Wochen | § 15a InsO-Antragspflicht |

---

## 7) Workflow-Engine-Implementierung

### Empfohlene Plattformen

- **Bryter** (https://bryter.com) — No-Code Legal Workflow
- **Josef** (https://www.josef.legal) — Document Automation
- **Documate** (https://www.documate.org) — Doc-Assembly fuer Legal
- **Neota Logic** — Enterprise-Workflow
- **Custom**: Node.js + JSON Schema + React Hook Form

### Architektur

```
┌─────────────────────────────────────────┐
│  Frontend (React Hook Form)             │
│  Kaskadierende Fragen, JSON Schema       │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│  Business-Logic-Engine                  │
│  Conditional Logic, Validierung,        │
│  Trigger-Events, Fristen                │
└────────────────┬────────────────────────┘
                 │
   ┌─────────────┼─────────────┐
   │             │             │
┌──▼──┐    ┌────▼─────┐  ┌────▼──────┐
│ DOC │    │ Fristen-  │  │ Notar-    │
│ ASM │    │ Engine    │  │ Paket-   │
│     │    │ iCal/Out- │  │ ZIP-      │
│     │    │ look      │  │ Export   │
└─────┘    └───────────┘  └───────────┘
```

### Output-Formate

- **DOCX** (Microsoft Word): Satzung, SHA, GF-Vertrag, Beiratsordnung
- **PDF** (signiertes Endprodukt): nach Notar-Beurkundung
- **XLSX** (Excel): Cap Table, Fristen-Liste, Behoerden-Checkliste
- **iCal/ICS**: Fristen-Kalender fuer Outlook/Apple Calendar
- **JSON**: Daten-Export fuer Buchhaltung / CRM
- **ZIP**: Notar-Paket mit allen Urkunden

---

## 8) Validierungs-Regeln

### Hartes Validierungs-Block

- Stammkapital < Mindesthoehe -> Block
- Anteilssumme != 100 % -> Block
- Pflichtfeld nicht ausgefuellt -> Block
- Bei Sacheinlage: kein Werthaltigkeits-Nachweis -> Block
- Bei Minderjaehrigem: keine Familiengericht-Genehmigung -> Block

### Weiches Validierungs-Warnung

- Anteilsverteilung 50/50 ohne Stichentscheid -> Warnung Patt-Risiko
- Vesting fehlt bei Multi-Gruender -> Warnung Bad-Leaver-Risiko
- Bezugsrechtsausschluss bei kuenftiger KE geplant ohne sachliche Begruendung -> Warnung Anfechtungs-Risiko
- Minderheits-Gesellschafter-GF ohne Sperrminoritaet -> Warnung SV-Pflicht
- Wettbewerbsverbot ohne Karenz -> Warnung Sittenwidrigkeit
- Marken-Konflikt erkannt -> Warnung mit Vorschlag-Alternativen

---

## 9) Reporting und Audit-Trail

### Audit-Trail

Jede Eingabe und jede Entscheidung im Workflow wird protokolliert mit:

- Zeitstempel
- Benutzer
- Eingabe-Wert
- Validierungs-Status
- Triggered Skills / Documents

### Reporting

Am Ende des Intakes wird automatisch generiert:

- **Datenblatt Gruendung** (alle Eckdaten)
- **Cap Table** initial
- **Pflichten-Checkliste** mit Fristen
- **Stoppschilder-Liste** (was zwingend Anwalt / Notar / Steuerberater)
- **Notar-Paket** vorbereitet
- **Behoerden-Pflichten-Kalender** als iCal

---

## 10) Beispielhafter Knoten-Inhalt JSON

```json
{
  "node_id": "intake_class_shares",
  "title": "Class-Shares-Festlegung",
  "question": "Sollen Anteilsklassen schon bei Gruendung eingefuehrt werden?",
  "type": "single-choice",
  "options": [
    {
      "id": "only_common",
      "label": "Nur Common Shares — Class-Shares spaeter einfuehren",
      "next": "intake_vesting",
      "trigger_skill": "gesellschaftsgruender-gesellschaftsvertrag-gmbh",
      "warning_if": [
        {
          "condition": "investor_planned_within_12_months == true",
          "message": "Bei absehbarem Investor empfohlen, schon jetzt Class-Shares vorzusehen oder genehmigtes Kapital fuer Class B"
        }
      ]
    },
    {
      "id": "common_and_b",
      "label": "Common + Class B (Vorbereitung Investor)",
      "next": "intake_b_share_terms",
      "trigger_skill": "gesellschaftsgruender-share-classes-a-b-c"
    },
    {
      "id": "multi_class",
      "label": "Multi-Class (Common + A + B + C)",
      "next": "intake_multi_class_governance",
      "trigger_skill": "gesellschaftsgruender-share-classes-a-b-c",
      "warning": "Multi-Class-Strukturen sind komplex und teuer beim Notar; nur bei klarer Investoren-Roadmap empfohlen"
    }
  ]
}
```

---

## 11) Anschluss

- `gesellschaftsgruender-gruender-intake` — Intake-Fragen im Detail
- `gesellschaftsgruender-cap-table` — Cap-Table-Generation
- `gesellschaftsgruender-klauselkatalog-bilingual` — Klauseln im Volltext
- `gesellschaftsgruender-kommandocenter` — Gesamt-Workflow
