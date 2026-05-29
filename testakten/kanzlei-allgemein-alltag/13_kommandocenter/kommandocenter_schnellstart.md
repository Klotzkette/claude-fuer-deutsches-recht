# Kommandocenter — Schnellstart-Anleitung

**Dokument:** KZ-2026-INST-001  
**Erstellt:** 20.05.2026  
**Verfasserin:** Jana Reuter  
**Zweck:** Einführungsleitfaden und erwartetes Systemverhalten beim ersten Aufruf des Kanzlei-Assistenten in einem neuen Mandat oder einer Routineaufgabe

---

## 1. Was ist das Kommandocenter?

Das Kommandocenter ist die zentrale Eingabe-Schnittstelle der Kanzlei, über die alle Kanzleiaufgaben — Aktenanlage, Fristberechnung, Schriftsatzentwurf, GwG-Prüfung, Zeiterfassung, Buchhaltung, HR — angestoßen werden. Es nimmt formlose Nutzereingaben entgegen und leitet die Aufgaben strukturiert an die richtigen Arbeitsbereiche weiter.

---

## 2. Beispiel-Nutzereingabe (Mischauftrag)

> **Nutzer:** "Ich habe eine neue Sache, wahrscheinlich Anteilskauf mit Immobilienbezug, Mandant schickt Ausweis und Registerauszug, Frist nächste Woche, bitte Akte anlegen, GwG prüfen und später eine Replik in einer anderen Sache vorbereiten."

---

## 3. Erwartetes Systemverhalten — Schritt für Schritt

### 3.1 Ampel-Bewertung Mandatsannahme / GwG

Das System gibt sofort eine Ampel-Bewertung für die Mandatsannahme nach dem Geldwäschegesetz (GwG) aus:

**Ampel GELB** — Mandate mit erhöhtem Prüfaufwand (Anteilskauf mit Immobilienbezug):  
Anteilskäufe mit Grundstücksbezug sind nach § 2 Abs. 1 Nr. 7 und Nr. 10 GwG geldwäscherechtlich relevant. Vor Mandatsannahme ist eine Identifizierung des Mandanten und der wirtschaftlich Berechtigten erforderlich.

Bei Hinweisen auf PEP-Status (politisch exponierte Person) oder Hochrisikoland → automatisch **ROT**.

### 3.2 Drei gezielte Rückfragen (nicht mehr)

Das System stellt exakt drei Rückfragen — keine langen Checklisten, keine Skill-Aufzählung:

1. **Handelt der Mandant auf eigene Rechnung?**  
   (Relevant für: wirtschaftlich Berechtigter nach § 3 GwG; bei Handeln für Dritte gelten verstärkte Sorgfaltspflichten)

2. **Wer sind die wirtschaftlich Berechtigten, und gibt es PEP-Bezug?**  
   (Relevant für: § 15 GwG verstärkte Sorgfaltspflichten; Transparenzregister-Abgleich erforderlich)

3. **Gibt es eine konkrete Frist — Datum und Uhrzeit?**  
   (Relevant für: Fristenkontrolle, Ressourcenplanung, Notfallprozess bei beA-Ausfall)

### 3.3 Routing nach Klärung der Rückfragen

Nach Beantwortung der drei Fragen wird die Aufgabe strukturiert geroutet:

| Arbeitsschritt | Ziel-Ordner / Modul | Ergebnis |
|---------------|--------------------|---------:|
| Intake — Identifizierung Mandant | `12_mandatsannahme_gwg/` | GwG-Fragebogen, Ausweiskopie (geschützt) |
| Akte anlegen | Akten-Root, Unterordner 01–14 | Aktenzeichen, Aktenblatt |
| Mandatsannahme / GwG prüfen | `12_mandatsannahme_gwg/` | GwG-Freigabe oder Ablehnung |
| Kontoblatt anlegen | `12_mandatsannahme_gwg/mandatskontoblatt_*` | Forderungs- und Vergütungsübersicht |
| Frist eintragen | `08_hr_kalender/` | Fristenkalender, Jour-fixe-Agenda |
| Replik-Vorbereitung | `03_schreibcanvas/` | Schreib-Canvas-Karten, Rohentwurf |

**Wichtig:** Replik-Vorbereitung wird als **Folgeaufgabe** in die Offenliste aufgenommen und nicht mit der GwG-Prüfung vermischt. Erst nach Mandatsannahme und Aktenanlage wird die Replik bearbeitet.

### 3.4 Personalausweis — Handhabung

Der Ausweis wird **nicht** vom System transkribiert oder inhaltlich verarbeitet. Das System verlangt:

- Geschützte Ablage (verschlüsselt, Zugriff nur durch Jana Reuter)
- Bestätigung, dass Identifizierung nach § 8 GwG durchgeführt wurde
- Erfassung von Name, Geburtsdatum, Ausstellungsdatum, Ausweisnummer und ausstellende Behörde in strukturierter Form im GwG-Fragebogen (nicht im Klartext-Log)

---

## 4. Was das System nicht tut

| Verbotenes Verhalten | Begründung |
|---------------------|-----------|
| Alle Skills aufzählen | Überwältigt den Nutzer; nicht zielführend |
| Mehr als drei Rückfragen auf einmal stellen | Erzeugt Rückfrage-Stau; Nutzer verliert Überblick |
| Replik und GwG gleichzeitig bearbeiten | Qualitätsverlust durch Aufmerksamkeitsteilung |
| Ausweis-Inhalt transkribieren | Datenschutz; § 8 GwG verlangt Einsichtnahme, nicht Kopie im System |
| Automatische Mandatsannahme ohne Prüfung ausgeben | GwG-Pflicht; Mandatsannahme erfordert menschliche Freigabe |
| Frist berechnen ohne Datum-Bestätigung | Fehlerrisiko; Frist nur nach Bestätigung durch Anwältin |

---

## 5. Offenliste — Folgeaufgaben

Nach Abschluss der Mandatsannahme werden alle Folgeaufgaben in die Offenliste `07_tagesabschluss/offene_punkte.md` und in die Agenda `08_hr_kalender/jour_fixe_agenda.md` übertragen:

Beispiel für den oben beschriebenen Mischauftrag:

- [ ] **GwG-Fragebogen** ausfüllen und freigeben — Verantwortlich: Jana Reuter — Frist: vor erster Beratungsleistung
- [ ] **Ausweiskopie** geschützt ablegen — Verantwortlich: Jana Reuter — Frist: bei Mandatsannahme
- [ ] **Transparenzregister** prüfen auf wirtschaftlich Berechtigte — Verantwortlich: Jana Reuter — Frist: vor Tätigkeitsbeginn
- [ ] **Mandatsvereinbarung** inkl. KI/Datenschutz-Klausel versenden — Verantwortlich: Jana Reuter — Frist: vor erster Leistung
- [ ] **Replik vorbereiten (andere Sache)** — Verantwortlich: Mara Klein (Canvas), Jana Reuter (Freigabe) — Frist: nach GwG-Abschluss, vor Fristablauf der Repliksache

---

## 6. Schnellreferenz Aktenzeichen-Schema

Das Kanzlei-Aktenzeichen folgt dem Schema:

```
JJJJ-[RECHTSGEBIET]-[LAUFENDE NUMMER]
```

Beispiele:
- `2026-MIET-004` — Mietrechtsache Nr. 4 im Jahr 2026
- `2026-GMBH-001` — GmbH-/Gesellschaftsrecht Nr. 1 im Jahr 2026
- `2026-ARB-002` — Arbeitsrecht Nr. 2 im Jahr 2026

Gerichtsverfahren erhalten zusätzlich das gerichtliche Aktenzeichen, z. B.:  
`2026-MIET-004 | AG Mitte 12 C 88/26`

---

## 7. Systemvoraussetzungen und Integrationen (Zielzustand)

| Integration | Status heute | Zielzustand |
|-------------|:-----------:|------------|
| Outlook / E-Mail | verbunden | laufend |
| beA | simuliert | nativer beA-Client |
| Fristenkalender | manuell | Sync mit Kanzleisoftware |
| DATEV / Buchhaltung | nicht angebunden | DATEV-Online-Connector |
| ELSTER | über Steuerkanzlei | ggf. Direktanbindung |
| Lohnsoftware | nicht angebunden | Lexware / DATEV Lohn |
| Transparenzregister | manuell abrufbar | API-Abfrage (kostenpflichtig) |

---

*Dokument KZ-2026-INST-001 — Erstellt: 20.05.2026 — Jana Reuter, Kanzlei Reuter Rechtsanwälte, Lindenstraße 14, 10969 Berlin. Testdaten.*
