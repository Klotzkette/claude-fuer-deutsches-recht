# Umformulierung — Methodik und Softening-Techniken

Plugin `email-umformulierer-berufsrecht`: Technische und linguistische Grundlagen

---

## Überblick

Das Plugin `email-umformulierer-berufsrecht` wurde entwickelt, um emotionale, berufsrechtlich riskante Korrespondenz in BORA/BRAO-konforme Formulierungen zu überführen. Es ist kein Rechtschreibkorrektor, sondern ein semantischer Transformer, der auf das spezifische Spannungsfeld zwischen mandatsbedingtem Interessendruck und berufsrechtlicher Sachlichkeitspflicht ausgerichtet ist.

---

## Detektionsstufen

Das Plugin arbeitet in drei Detektionsstufen:

### Stufe 1 — Hartes Flagging

Sofortige Markierung folgender Muster:
- Strafrechtliche Unterstellungen ohne Tatsachenbasis (Betrug, Nötigung, Erpressung als direkte Zuschreibung)
- Persönlichkeitsbezogene Herabsetzungen (Berufseignungszweifel, Intelligenzkritik)
- Drohformeln, die über legitimen Rechtsverfolgungsdruck hinausgehen
- Versandzeit zwischen 21:00 und 07:00 Uhr (Warnhinweis, kein Blocken)

### Stufe 2 — Mittleres Flagging

- Sarkasmus und Ironie in Formulierungen
- Übertriebene Quantifizierungen („immer", „nie", „ausnahmslos")
- Emotionsbeladene Adjektive ohne sachlichen Gehalt (z.B. „dreist", „unverschämt", „absurd")
- Unbelegt gebliebene Werturteile

### Stufe 3 — Weiche Hinweise

- Passiv-aggressive Formulierungen
- Unnötige Wiederholungen von bereits kommunizierten Positionen
- Sehr lange, verschachtelte Sätze, die in einem Spannungszustand entstanden sind

---

## Softening-Techniken

### Technik 1: Tatsachendistillation

Aus einer emotional aufgeladenen Passage wird der sachliche Kern extrahiert:

**Vorher:** „Seit 18 Monaten hinhalten, belügen, taktieren."

**Nachher:** „Die Übermittlung der erbetenen Unterlagen für die Geschäftsjahre 2022 und 2023 ist trotz wiederholter Fristen bisher ausgeblieben. Wir bitten um Klärung, welche konkreten Hinderungsgründe einer Übersendung entgegenstehen."

### Technik 2: Vorwurf in Rechtsfrage überführen

**Vorher:** „Ihr Verhalten ist sittenwidrig und riecht nach Prozessbetrug."

**Nachher:** „Wir behalten uns vor, die Verweigerung der Auskunft nach § 166 HGB auf ihre rechtliche Qualifikation — einschließlich möglicher Schadensersatzansprüche — zu prüfen."

### Technik 3: Drohung in Rechtsmittelankündigung

**Vorher:** „Wenn Sie nicht bis Freitag, 28.02.2026, die Unterlagen herausgeben, ziehen wir die Insolvenz durch."

**Nachher:** „Sollte eine vollständige Übermittlung der angeforderten Unterlagen nicht bis zum 28.02.2026 erfolgen, werden wir uns veranlasst sehen, alle zur Verfügung stehenden rechtlichen Maßnahmen zu ergreifen und deren Zulässigkeit im konkreten Fall zu prüfen."

### Technik 4: Persönlichen Angriff neutralisieren

**Vorher:** „Wenn Sie in 34 Jahren Praxis nichts anderes gelernt haben als zu mauern, sollten Sie überlegen, ob Sie den falschen Beruf gewählt haben."

**Nachher:** [Passage wird vollständig gestrichen — kein Sachbeitrag, kein Ersatz notwendig.]

### Technik 5: Emotionale Selbstoffenbarung entfernen

**Vorher:** „ich schreibe Ihnen jetzt um kurz vor zwei Uhr nachts, weil ich nicht schlafen kann vor Wut"

**Nachher:** [Passage wird vollständig gestrichen — keine anwaltlich verwertbare Information.]

---

## Versionshistorie der Umformulierung (Kröll-E-Mail)

| Version | Datum | Bearbeiterin | Status |
|---|---|---|---|
| Original | 14.02.2026, 01:47 Uhr | RA Dr. Kröll (automatisch versandt) | Bereits abgesandt — kein Rückruf möglich |
| v1 | 14.02.2026, 09:12 Uhr | Plugin-Autovorschlag | Zu weich — verliert die Druckbotschaft |
| v2 | 14.02.2026, 10:44 Uhr | RAin Tannenkamp manuell adjustiert | Besser, aber noch Passivkonstruktionen |
| v3 | 14.02.2026, 11:30 Uhr | RAin Tannenkamp + Plugin-Überprüfung | BORA-konform — hätte versandt werden sollen |

Die v3-Fassung (EML 2026-02-14, Umformulierung) ist als Referenzbeispiel für die Plugin-Dokumentation vorgesehen.

---

## Grenzen des Plugins

Das Plugin kann keine Tatsachen erfinden und keine Rechtsposition verbessern, die inhaltlich schwach ist. Es kann nur die Sprache korrigieren. Wenn der Sachvortrag nicht trägt, hilft keine Umformulierung. Das Plugin warnt in solchen Fällen mit dem Hinweis: „Inhaltliche Substanz fehlt — Formulierungsanpassung allein löst das Problem nicht."

Außerdem hat das Plugin keine Versandsperrfunktion. Es kann die Originalversion nicht zurückhalten, wenn der Nutzer auf „Senden" drückt, bevor die Reformulierung abgeschlossen ist. Die technische Lösung (Outlook-Add-in mit Versionszwang) ist in Planung (vgl. Aktenstück 16).

---

Bearbeitungsstand: 22.04.2026 — RAin Yvonne Tannenkamp
