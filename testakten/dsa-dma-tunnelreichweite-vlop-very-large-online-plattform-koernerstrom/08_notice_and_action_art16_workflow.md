# Aktenstück 08 — Notice-and-Action-Verfahren nach Art. 16 DSA: Workflow-Analyse

**Az. Kanzlei:** KRS-2026-0318-DSA
**Bearbeitung:** RA Felix Wendland
**Stand:** 01. April 2026

---

## 1. Normgrundlage und BNetzA-Beanstandung

Art. 16 DSA verpflichtet Hosting-Anbieter — unabhängig von der VLOP-Eigenschaft — dazu, Mechanismen einzurichten, durch die jede Person oder Einrichtung einer Plattform das Vorhandensein von mutmaßlich illegalen Inhalten mitteilen (melden) kann (Notice). Der Anbieter muss diese Meldungen zeitnah, sorgfältig und ohne Willkür bearbeiten und entsprechende Maßnahmen treffen (Action).

Die Bundesnetzagentur hat im Mahnschreiben vom 02. April 2026 (Az. BNetzA-DSC-2026-188) folgenden Verstoß benannt:

> "Im Zeitraum Oktober 2025 bis Februar 2026 wurden Meldungen zu Hassrede-Inhalten auf Halmweise.de mit einer medianen Bearbeitungszeit von 11,3 Werktagen bearbeitet. Dies entspricht nicht der Anforderung des Art. 16 Abs. 6 DSA, wonach Meldungen ohne unnötige Verzögerung zu bearbeiten sind. Bei klar illegalen Inhalten (z.B. öffentlicher Volksverhetzung nach § 130 StGB) sind Maßnahmen unverzüglich zu ergreifen."

---

## 2. Iststand-Analyse Notice-and-Action-Prozess

### 2.1 Aktueller Workflow (vor Optimierung)

```
Nutzer meldet Inhalt
        ↓
Automatische Eingangsbestätigung (sofort)
        ↓
Manuelle Erstsichtung Trust & Safety Queue
(Bearbeitungszeit: 3-8 Werktage wegen Personalengpass)
        ↓
Inhaltliche Prüfung durch moderator
(Bearbeitungszeit: 2-5 Werktage)
        ↓
Entscheidung: Belassen / Einschränken / Entfernen
        ↓
Benachrichtigung Meldender (Art. 16 Abs. 5 DSA)
Benachrichtigung Inhaltsersteller (Art. 17 DSA)
```

**Mediane Gesamtdauer:** 11,3 Werktage (Oktober 2025 bis Februar 2026)

**Hauptursachen der Verzögerung:**
- Unzureichende Personalkapazität (180 Trust & Safety Mitarbeiter für 51 Mio. Nutzer)
- Fehlende KI-Vorsortierung nach Risikostufe
- Keine priorisierten Warteschlangen für Hochrisiko-Inhalte

---

### 2.2 Soll-Workflow (nach Optimierung)

```
Nutzer meldet Inhalt
        ↓
KI-Klassifikation innerhalb 60 Sekunden:
  HOCHRISIKO (§ 130 StGB, CSAM) → Priority-Queue
  STANDARDRISIKO → Standard-Queue
        ↓
Priority-Queue:
  Sichtung durch Senior-Moderator: max. 4 Stunden
  Entscheidung und Aktion: max. 24 Stunden Gesamtdauer
        ↓
Standard-Queue:
  Sichtung: max. 24 Stunden
  Entscheidung: max. 72 Stunden Gesamtdauer
        ↓
Benachrichtigung Meldender (Art. 16 Abs. 5 DSA): sofort nach Entscheidung
Benachrichtigung Inhaltsersteller (Art. 17 DSA): sofort nach Entscheidung
Weiterleitungspflicht (Art. 18 DSA): bei strafrechtlich relevantem Inhalt an Strafverfolgungsbehörden
```

---

## 3. Anforderungen an die Meldung (Art. 16 Abs. 2 DSA)

Für eine qualifizierte Meldung verlangt Art. 16 Abs. 2 DSA folgende Mindestangaben:

- Hinreichende Begründung, warum der Inhalt als illegal angesehen wird
- Genaue Bezeichnung des Speicherorts (URL)
- Name und Kontaktdaten des Meldenden (soweit Einzelperson)
- Erklärung, dass die Meldung in gutem Glauben erfolgt

Meldungen, die diese Mindestanforderungen nicht erfüllen, müssen nicht vorrangig bearbeitet werden, sind aber nicht zurückzuweisen; der Meldende ist zur Ergänzung aufzufordern.

---

## 4. Pflichten nach der Entscheidung (Art. 16 Abs. 5, Art. 17 DSA)

### 4.1 Benachrichtigung des Meldenden (Art. 16 Abs. 5 DSA)

Der Anbieter hat den Meldenden unverzüglich über die getroffene Entscheidung und die Widerspruchsmöglichkeit zu informieren.

### 4.2 Begründungspflicht gegenüber dem Inhaltsersteller (Art. 17 DSA)

Bei jeder Entscheidung, einen Inhalt zu entfernen, einzuschränken oder ein Konto zu sperren, muss der Anbieter dem Inhaltsersteller eine klare und spezifische Begründung zukommen lassen, einschließlich Angaben zu den Rechtsmitteln (intern und extern).

### 4.3 Interne Beschwerdestelle (Art. 20 DSA)

Nutzer können Entscheidungen bei der internen Beschwerdestelle anfechten. Für VLOPs gelten erweiterte Anforderungen — vgl. Aktenstück 09.

---

## 5. Statistische Anforderungen und Reporting

Art. 15 DSA und Art. 42 DSA verlangen Statistiken über den Notice-and-Action-Prozess:

| Metrik | Erforderlich nach |
|---|---|
| Anzahl erhaltener Meldungen | Art. 15 Abs. 1 lit. c DSA |
| Anzahl nach Inhaltskategorie | Art. 42 Abs. 2 lit. a DSA |
| Medianer Bearbeitungszeitraum | Art. 15 Abs. 1 lit. d DSA |
| Ergebnisse (Entfernung/Belassen) | Art. 15 Abs. 1 lit. c DSA |
| Widersprüche und Ergebnis | Art. 15 Abs. 1 lit. c DSA |
| Fehlerquoten | Art. 42 Abs. 2 lit. b DSA |

---

## 6. Empfehlungen an Mandantin

1. Unverzügliche Einführung KI-gestützter Vorsortierung (Frist: 15.06.2026).
2. Erhöhung Trust & Safety Personal um mind. 30 Stellen (Frist: schrittweise bis 01.08.2026).
3. Internes SLA: 24 Stunden Hochrisiko / 72 Stunden Standard.
4. Monatliches Reporting an die Geschäftsführung.
5. Statistiken im H1/2026-Transparenzbericht vollständig darstellen.

---

## 7. Rechtsgrundlagen

- Art. 16 DSA (EU) 2022/2065 — Notice-and-Action
- Art. 17 DSA — Begründungspflicht
- Art. 18 DSA — Weiterleitungspflicht an Strafverfolgungsbehörden
- Art. 20 DSA — Interne Beschwerdestelle
- § 130 StGB — Volksverhetzung

**Quellen:**
- Verordnung (EU) 2022/2065 (DSA), EUR-Lex: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022R2065
- § 130 StGB, dejure.org: https://dejure.org/gesetze/StGB/130.html

---

*Bearbeitung: RA Felix Wendland*
*Stand: 01. April 2026*
