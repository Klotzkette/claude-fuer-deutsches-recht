# Strategiememorandum — RA Lukas Drosten

**Aktenstück:** 20  
**Datum:** 13.05.2026  
**Mandantin:** Frischetrans Mittelrhein GmbH  
**Verfasser:** RA Lukas Drosten, Fachanwalt für IT-Recht  
**Vertraulich — Anwaltliches Berufsgeheimnis**

---

## 1. Überblick und Gesamtlage

Sieben Tage nach dem Ransomware-Angriff lässt sich eine erste fundierte strategische Gesamtbewertung vornehmen. Das Mandat hat sich von einer reinen Notfall-Reaktion zur umfassenden IT-rechtlichen Beratung entwickelt und umfasst nunmehr folgende Komplexe:

| Komplex | Priorität | Status |
|---|---|---|
| A. Datenschutz / DSGVO (Art. 33, 34, 35) | Hoch | Erstmeldungen erstattet, DSFA eingeleitet |
| B. NIS2 / BSI-Meldung | Hoch | Erstattet |
| C. Strafanzeige ZAC Mainz | Hoch | Erstattet |
| D. ProcessSpark — SLA-Verletzung / Schadensersatz | Sehr hoch | Klageandrohung raus, Frist bis 26.05.2026 |
| E. KI-VO — PalettenAuge AI | Mittel | Analyse abgeschlossen, Maßnahmen eingeleitet |
| F. Open Source Compliance TourPlanner | Mittel | Audit abgeschlossen, Handlungsoptionen identifiziert |
| G. Betriebsrat / Mitarbeiter | Hoch | Anhörung erledigt, BV-Entwürfe folgen |
| H. Versicherung CyberCovered | Hoch | Gemeldet, Regulierung in Lauf |
| I. Kundenkommunikation / Schadensersatz Kunden | Mittel-Hoch | Anschreiben raus, Frischbäcker AG zeigt Ansprüche |

---

## 2. Rechtliche Kernrisiken und Risikobewertung

### 2.1 DSGVO-Bußgeldrisiko

**Risikoprofil:** Mittel bis Hoch

Der LfDI RLP hat die Meldung entgegengenommen und Rückfragen gestellt. Die entscheidende Frage ist, ob der LfDI ein Bußgeldverfahren eröffnet. Relevante Gesichtspunkte:

- **Positiv:** Frischetrans hat alle Meldepflichten fristgerecht erfüllt (Art. 33 DSGVO: innerhalb 72 h; BSI: innerhalb 24 h). Proaktive Transparenz gegenüber Behörden.
- **Negativ:** Die TOMs (technisch-organisatorische Maßnahmen) waren zum Zeitpunkt des Angriffs für die Verarbeitung von Art.-9-Daten (Gesundheitsdaten BEM) unzureichend (fehlende at-rest-Verschlüsselung, unzureichendes Patch-Management).
- **Mildernd:** Die unmittelbaren Mängel (Patch-Rückstand) sind auf den IT-Dienstleister ProcessSpark zurückzuführen. Frischetrans hat die Patchverantwortung vertraglich an ProcessSpark übertragen. Dies mindert das eigene Verschulden, entlastet aber nicht vollständig.

**Bußgeldrisiko-Schätzung:** 50.000–350.000 EUR (Art. 83 Abs. 4 DSGVO, Verstöße gegen Art. 32 DSGVO; Bußgeldrahmen 10 Mio. EUR / 2 %)

**Strategie:** Vollständige Kooperation mit LfDI, schnelle Umsetzung der DSFA-Maßnahmen, Vorlage eines detaillierten Verbesserungsplans — dies mildert Bußgelder erheblich.

### 2.2 ProcessSpark — Klagerisiko und Einigungschance

**Risikoprofil:** Hoch (Klagerisiko für ProcessSpark), Mittel (Prozessrisiko für Frischetrans)

Die Haftungssituation gegen ProcessSpark ist gut. Die Beweislage (SAP Security Note, Patch-Log, forensischer Bericht) ist stark. Der einzige nennenswerte Unsicherheitsfaktor ist die Haftungsbeschränkungsklausel (§ 16 Vertrag), deren Wirksamkeit aber bezweifelt werden darf.

**Realistische Einigungschance:** 60–70 % (außergerichtliche Einigung nach Klageandrohung). ProcessSpark hat kein Interesse an einem öffentlichen Prozess mit Aufmerksamkeit auf CVE-2026-0712-Patchversagen.

**Strategie:** Die Frist (26.05.2026) wird konsequent gehalten. Bei Nichtreaktion: Klageeinreichung am LG Mainz (AZ 3 O 88/26). Gleichzeitig Offenheit für Mediationsverfahren oder EU-ODR-Verhandlung (Skill `fachanwalt-it-recht-it-vertrag-verhandlung-eu-odr`).

**Alternative:** Sanierungsverhandlung mit ProcessSpark: Klage wird ausgesetzt gegen Zusage erhöhter SLAs, Kostenerstattung, Vertragsanpassung (neue Patchpflichten). Sinnvoll, wenn Mandantin den Vertrag fortsetzen möchte.

### 2.3 Kundenforderungen (Frischbäcker AG)

**Risikoprofil:** Mittel

Frischbäcker AG hat anwaltliche Beratung eingeholt und prüft Schadensersatzansprüche. Hauptargument wird der Betriebsunterbrechungsschaden (Lieferausfall 07.05.2026) sein.

**Strategie:** CyberCovered AG (Drittparteideckung) informieren. Force-Majeure-Einwand aus Rahmenvertrag prüfen. Ggf. Vergleich anbieten, wenn Forderung überschaubar.

### 2.4 KI-VO — Fristrisiko (02.08.2026)

Die EU-KI-VO Hochrisikopflichten gelten ab 02.08.2026. Bis dahin sind noch **81 Tage**. Das ist knapp. PalettenAuge AI muss bis dahin entweder:
- vollständig konform gemacht werden (Konformitätsbewertung durch DachAuge, Betriebsvereinbarung, Human-Oversight-Prozess), oder
- in eingeschränktem Modus betrieben werden (keine Personaldaten-Einspeisung).

**Risiko bei Nichthandeln:** Bußgeld bis 15 Mio. EUR (Art. 99 KI-VO) — für KMU deutlich reduziert, aber empfindlich.

### 2.5 Open Source / AGPL

Kurzfristig kein behördliches Risiko. Aber Abmahnungsrisiko durch ScheduleHero Foundation ist real. Die Kosten einer außergerichtlichen Einigung (kommerzielle Lizenz oder freiwillige Code-Offenlegung) sind überschaubar im Vergleich zu einem Rechtsstreit.

---

## 3. Mandatspriorisierung (Empfehlung)

| Priorität | Maßnahme | Frist | Zuständig |
|---|---|---|---|
| 1 | ProcessSpark: Frist überwachen (26.05.2026) | 26.05.2026 | RA Drosten |
| 2 | LfDI: DSFA und Verbesserungsplan einreichen | 22.05.2026 | RA Drosten + DSB Feilke |
| 3 | Betriebsrat: Betriebsvereinbarung KI | 30.06.2026 | RA Drosten |
| 4 | DachAuge: Konformitätsdokumentation anfordern | 20.05.2026 | RA Drosten |
| 5 | AGPL: Kontaktaufnahme ScheduleHero Foundation | 20.05.2026 | RA Drosten |
| 6 | Versicherung: Schadensdokumentation komplett | 31.05.2026 | Frischetrans + RA Drosten |
| 7 | Mitarbeiterversammlung organisieren | 20.05.2026 | HR + BR |
| 8 | ProcessSpark-Klage vorbereiten (Schriftsatz LG Mainz) | Bis 10.06.2026 | RA Drosten |

---

## 4. Gesamteinschätzung

Der Mandantin ist zu bescheinigen, dass sie in dieser Ausnahmesituation trotz enormer operativer Belastung kluge Entscheidungen getroffen hat: keine Lösegeldzahlung, sofortige Behördenkommunikation, proaktive Mitarbeiterinformation, konstruktive Zusammenarbeit mit der Kanzlei. Das ist der Idealfall einer datenschutzrechtlichen Incident Response.

Die größten verbleibenden Risiken sind (a) ein mögliches LfDI-Bußgeld (mittelbar durch ProcessSparks Patchversagen verursacht), (b) die KI-VO-Compliance-Frist für PalettenAuge AI und (c) die AGPL-Compliance-Frage für TourPlanner.

Der Fall gegen ProcessSpark ist juristisch stark und verspricht hohe Erfolgschancen.

**Gesamtschadenspotenzial Mandantin (worst case):** ca. 1,2–2,0 Mio. EUR  
**Erwartetes Regressvolumen aus ProcessSpark:** ca. 500.000–700.000 EUR (netto nach Prozesskosten)  
**Versicherungsdeckung:** bis 5 Mio. EUR (abzügl. Selbstbehalt 25.000 EUR laut Police)  
**Netto-Belastung Mandantin (Schätzung):** ca. 100.000–400.000 EUR
