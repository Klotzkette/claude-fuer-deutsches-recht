# 1. Abfrage, Memo und Zielgruppenfassung

Diese Modi werden nach Aufbau oder Ergänzung des Untersuchungsbestands nur für eine konkrete Protokollabfrage, ein Untersuchungsmemo oder eine adressatengerechte Zusammenfassung geladen.

## Modus 3: Protokoll abfragen

Ausgelöst durch `/arbeitsrecht:untersuchung-abfrage`.

Gesamtes Protokoll lesen vor der Antwort. Antworttypen:

**Sachverhaltsabfrage** ("Was hat [Person] zu [Thema] gesagt?"):
Aus den Protokolleinträgen antworten, Eintrags-IDs zitieren. Falls das
Protokoll nichts enthält: "Zu [Thema] liegen in diesem Untersuchungsprotokoll
([N] Einträge gesichtet) keine Erkenntnisse vor. Dies sollte ggf. als
Beweislücke erfasst werden."

**Widerspruchsabfrage** ("Wo widersprechen sich die Schilderungen?"):
Alle widerspricht_eintrag-Verknüpfungen zeigen. Pro Widerspruch: Was ist
der Konflikt, welche Einträge stehen im Widerspruch, welche dokumentarische
Evidenz besteht?

**Deckungsabfrage** ("Was fehlt noch?" / "Wo haben wir Lücken?"):
quellen-checkliste.yaml und beweislücken im log.yaml auslesen. Melden:
- Noch offene Checklistenpunkte
- Protokollierte Beweislücken
- Schilderungen, die auf bisher nicht erhobene Quellen hinweisen

**Stärkeabfrage** ("Was ist die stärkste Evidenz zu jeder Frage?"):
Für jede Untersuchungsfrage: höchstbewertete Protokolleinträge, dokumentarische
Bestätigungen und ungelöste Widersprüche — frageweise strukturiert.

---

## Modus 4: Memo entwerfen oder aktualisieren

Ausgelöst durch `/arbeitsrecht:untersuchungs-memo`.

### Erstmalige Erstellung

Gesamtes Protokoll lesen. Vor dem Entwurf prüfen (Warnung falls nicht erfüllt):
- Mindestens ein Eintrag pro offener Untersuchungsfrage
- Einträge für Beschwerdeführer/in und Beschuldigte/n vorhanden
- Quellencheckliste geprüft (hochprioritäre offene Punkte flaggen)

Memo in folgender Struktur:

```markdown
VERTRAULICH — INTERNE UNTERSUCHUNG — [Datum]

---

**VERMERK**

An: [Anwalt eintragen]
Von: [Anwalt eintragen]
Datum: [Datum]
Betr.: Interne Untersuchung — [Sachbezeichnung]
Stand: VORENTWURF

---

## Zusammenfassung

[2–3 Abschnitte: Vorwurf in eigenen Worten, Untersuchungsumfang und
Methodenüberblick, wesentliche Ergebnisse in Stichpunkten (Bestätigt /
Nicht bestätigt / Unklar), empfohlene Maßnahmen. Wird zuletzt geschrieben,
erscheint zuerst.]

---

## Hintergrund und Untersuchungsumfang

**Auslöser:** [Was hat die Untersuchung ausgelöst]

**Untersuchte Vorwürfe:**
[Jede Frage aus dem Protokoll als nummerierter Vorwurf]

**Nicht Untersuchtes:** [Was ausdrücklich ausgeklammert wurde und warum]

**Zeitraum des vorgeworfenen Verhaltens:** [Daten]
**Untersuchungszeitraum:** [Datum Eröffnung] bis [aktuell oder Abschluss]

---

## Methodik

**Durchgeführte Anhörungen:**
| Person | Funktion | Datum | Hinweise |
|---|---|---|---|

**Gesichtete Dokumente:**
[Zusammenfassung nach Dokumentenkategorien, Umfang, Zeitraum.
Vollständiges Dokumentenprotokoll separat geführt.]

**Sonstige Quellen:**
[Richtlinien, Personalakten, sonstige Quellen aus der Checkliste]

**Einschränkungen:** [Angeforderte aber nicht erhaltene Quellen, sonstige Grenzen]

---

## Sachverhaltliche Feststellungen

*[Nach Fragen gegliedert — ein Abschnitt pro Vorwurf. Nicht nach Zeuge,
nicht rein chronologisch.]*

### Frage 1: [Vorwurf]

[Narrative Darstellung der Erkenntnislage. Eintrags-IDs in Klammern zitieren.
Wo Schilderungen im Widerspruch stehen: Widerspruch direkt benennen —
nicht glätten. Dokumentarische Belege mit Zitaten wenn bedeutsam.]

---

## Glaubwürdigkeitsbewertung

*[Eigenständiger Abschnitt. Nur Personen, deren Glaubwürdigkeit entscheidungserheblich
ist — d. h. wo das Ergebnis zu einer Frage davon abhängt, welche Schilderung
geglaubt wird.]*

### [Name/Funktion]

**Innere Konsistenz:** [Konsistent / Inkonsistent — konkrete Angaben]
**Bestätigung:** [Was an dokumentarischer oder sonstiger Evidenz stützt oder
erschüttert die Schilderung]
**Motiv:** [Anlass, die Schilderung zu kreditieren oder zu bezweifeln]
**Impression:** [Beobachtungen des Anwalts bei persönlicher Befragung —
sonst freilassen]
**Bewertung:** [Kreditieren / Nicht kreditieren / Teilweise kreditieren — mit Begründung]

---

## Einschlägige Regelungen

[Zum Tatzeitpunkt geltende Regelungen, die für die Fragen bedeutsam sind.
Version angeben. Keine nach dem Vorfall eingeführten Regelungen zitieren.]

---

## Ergebnisse

| Frage | Ergebnis | Grundlage |
|---|---|---|
| [Frage 1] | Bestätigt / Nicht bestätigt / Unklar | [Ein Satz] |

*Ergebnisse auf Basis des Beweismaßes der überwiegenden Wahrscheinlichkeit.*

---

## Empfehlungen

**Disziplinarische Maßnahmen:** [Falls zutreffend — Grundlage, nicht nur Ergebnis]
**Regelungs- oder Prozessänderungen:** [Falls ein Regelungsdefizit beigetragen hat]
**Schulungen:** [Falls angezeigt]
**Weitere Untersuchung:** [Noch nicht abgeschlossene Stränge]
**Monitoring:** [Erforderliche Nachverfolgung]

---

## Anlage A: Chronologie

[Aus Protokolleinträgen nach ereignis_datum sortiert — nicht nach protokoll_datum.
Format: Datum | Zusammenfassung | Quelle (Eintrags-ID)]

## Anlage B: Gesichtete Dokumente

[Übersichtstabelle aus dokumente-geprueft.yaml]
```

### Falls Memo bereits existiert — Aktualisierung

Memo und Protokoll lesen. Seit dem letzten Entwurf hinzugekommene Einträge
identifizieren.

Änderungen melden, dann fragen: "Soll das gesamte Memo überarbeitet werden
oder nur die betroffenen Abschnitte?"

Änderungen einarbeiten. Geänderte Abschnitte mit `[AKTUALISIERT: Datum]`
markieren bis zur Freigabe durch den Anwalt.

---

## Modus 5: Zielgruppen-Zusammenfassung

Ausgelöst durch `/arbeitsrecht:untersuchungs-zusammenfassung`.

Frage: Für wen ist die Zusammenfassung und welche Entscheidung oder Maßnahme
soll sie unterstützen?

**HR-Zusammenfassung** (für disziplinarische Entscheidung):
- Was ist passiert (Sachverhaltsdarstellung, keine Rechtsanalyse)
- Ergebnis zu jedem Vorwurf (Bestätigt / Nicht bestätigt / Unklar)
- Empfohlene Maßnahme
- Nicht enthalten: Glaubwürdigkeitsmethodik, Rechtsrisikoanalyse,
 anwaltliche Eindrücke
- Kopfzeile: "Vertraulich — Nur für HR — Keine Weitergabe"
- Keine Eintrags-IDs oder Dokumentenverweise

**Geschäftsführung / Aufsichtsrat** (für Governance-Entscheidung):
- Vorwurf und Umfang in einem Abschnitt
- Wesentliche Ergebnisse
- Unternehmensrelevanz / Expositionseinschätzung (nur grob — keine Detailrechtsanalyse)
- Ergriffene und geplante Maßnahmen
- Kopfzeile: "Vertraulich — Interne Untersuchung"

**Externe Bevollmächtigte** (für Prozessvorbereitung oder vertiefende Prüfung):
- Vollständiger Kontext einschließlich Rechtsrisikoanalyse
- Offene Beweisstränge
- Ungelöste Glaubwürdigkeitsfragen
- Dokumente mit erhöhter Prozeßrelevanz

---

## Was diese Skill nicht tut

- Disziplinarische Entscheidungen treffen — sie unterstützt die anwaltlichen
 Feststellungen, nicht die HR-Entscheidung
- Vertraulichkeitsschutz garantieren — Schutz hängt davon ab, wie die
 Untersuchung strukturiert und wie Materialien verteilt wurden
- Dokumente lesen, die technisch nicht verarbeitbar sind — solche Dateien
 für manuelle Prüfung flaggen
- Befragungen durchführen — Befragungsnotizen werden protokolliert,
 nicht selbst geführt
- Anhörungshinweise ersetzen — sie verfolgt, ob sie erteilt wurden,
 erteilt sie nicht selbst

## Quellenpflicht

Bei jeder Ausgabe zu Untersuchungsverfahren zitieren:
- Paragraf 26 BDSG (Beschäftigtendatenschutz, Verhältnismäßigkeit)
- Paragraf 87 Abs. 1 Nr. 6 BetrVG (Mitbestimmung bei technischer Überwachung)
- Beschäftigtendatenschutz: Paragraf 26 BDSG, Art. 5 und 6 DSGVO; Fachliteratur nur mit Nutzerquelle oder verifiziertem Live-Zugriff.
- Paragraf 626 BGB: Zwei-Wochen-Frist, Verdachtskündigung und Anhörung nur mit verifizierter BAG-Rechtsprechung oder Nutzerquelle vertiefen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
