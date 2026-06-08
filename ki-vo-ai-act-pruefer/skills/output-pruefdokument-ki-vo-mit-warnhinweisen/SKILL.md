---
name: output-pruefdokument-ki-vo-mit-warnhinweisen
description: "Erzeugt das abschliessende KI-VO-Pruefdokument mit Warnhinweisen, Tatsachenbasis und dokumentierbarer Begruendung. Deckt Art. 3 KI-System-Vermerk, Zweckbestimmung, GPAI/Chatbot-Abgrenzung, Art. 6 Abs. 2/Anhang III, Art. 6 Abs. 3-Rueckausnahme, Betreiber-Off-label-Nutzung, Pflichten, offene Punkte und Re-Evaluation ab. Output: strukturiertes Memo/Word/PDF für Compliance-Akte, Vorstand, Rechtsabteilung oder Kanzlei."
---

# Output: Prüfdokument KI-VO mit Warnhinweisen

## Zweck

Dieser Skill erstellt das abschließende Prüfdokument am Ende des KI-VO-Workflows. Es soll nicht nur Ergebnisse zusammenfassen, sondern die Einordnung so dokumentieren, dass später nachvollziehbar ist, auf welchen Tatsachen, Annahmen und Rechtskategorien die Entscheidung beruhte.

## Pflicht-Header

```text
MECHANISCHES PRÜFDOKUMENT — KI-VO
Verordnung (EU) 2024/1689

Keine Rechtsberatung. Dieses Dokument beruht auf den angegebenen Tatsachen und ersetzt keine anwaltliche Prüfung. Tatsachen, Zweckbestimmung, technische Eigenschaften und tatsächliche Nutzung können die Einordnung ändern.
```

## Mindeststruktur

### 1. Prüfauftrag und Quellen

- Mandant / Organisation
- Systemname und Version
- geprüfter Funktionszuschnitt: Modell, API, Chatbot, Fachworkflow, Gesamtprodukt
- Unterlagen: technische Dokumentation, Gebrauchsanweisung, Richtlinie, Logs, Verträge, Screenshots, Policies
- Stand der Prüfung und offene Tatsachen

### 2. KI-System-Einordnung

Aus `liegt-ki-system-vor-art-3-nr-1` übernehmen:

| Element | Ergebnis | Begründung |
|---|---|---|
| maschinenbasiertes System | Ja/Nein/Unklar | |
| Autonomiegrad | Ja/Nein/Unklar | |
| Adaptivität | Ja/Nein/Unklar/Nicht erforderlich | |
| explizite/implizite Ziele | Ja/Nein/Unklar | |
| Inferenz aus Eingaben | Ja/Nein/Unklar | |
| Output-Typ | Vorhersage/Inhalt/Empfehlung/Entscheidung | |
| Einfluss auf Umgebung | Ja/Nein/Unklar | |

Pflichttext:
```text
Auf Grundlage der vorliegenden Angaben ist das System [wahrscheinlich / wahrscheinlich nicht / offen] als KI-System im Sinne von Art. 3 Nr. 1 KI-VO einzuordnen. Entscheidend ist insbesondere [Inferenz/Automation/Output/Zweck]. Die bloße Automation wurde [nicht allein / zusammen mit Inferenz] bewertet; Autonomie wurde nicht als Vollautonomie verstanden.
```

### 3. Zweckbestimmung und tatsächliche Nutzung

Dokumentieren:
- Anbieter-Zweckbestimmung
- Betreiber-Zweck
- tatsächliche Nutzung in der Organisation
- verbotene oder ausgeschlossene Nutzungen
- vorhersehbarer Fehlgebrauch
- bekannte Abweichungen durch Mitarbeitende
- Re-Evaluation-Trigger

### 4. GPAI/Chatbot-Abgrenzung

Pflichttext bei allgemeinen Chatbots oder GPAI:
```text
Die allgemeine technische Nutzbarkeit eines GPAI-Systems oder Chatbots in Hochrisiko-Bereichen begründet für sich genommen noch keine Hochrisiko-Einstufung. Maßgeblich ist die konkrete Zweckbestimmung und der verantwortete Einsatz. Eine Hochrisiko-Prüfung nach Art. 6 Abs. 2 i.V.m. Anhang III ist erforderlich, wenn das System in einen entsprechenden Fachprozess integriert oder hierfür tatsächlich verwendet wird.
```

### 5. Risikoklassen-Ergebnis

| Prüfpunkt | Ergebnis | Fundstelle | Folge |
|---|---|---|---|
| Verbotene Praktik | Ja/Nein/Unklar | Art. 5 | |
| Hochrisiko Sicherheitsbauteil | Ja/Nein/Unklar | Art. 6 Abs. 1, Anhang I | |
| Hochrisiko Anhang III | Ja/Nein/Unklar | Art. 6 Abs. 2, Anhang III | |
| Rückausnahme | Greift/Greift nicht/Unklar | Art. 6 Abs. 3/4 | |
| Begrenztes Risiko | Ja/Nein/Unklar | Art. 50 | |
| GPAI-Modell/System | Ja/Nein/Unklar | Art. 3 Nr. 63/66, Art. 51 ff. | |

### 6. Anhang-III-Matrix

Auch bei negativem Ergebnis kurz dokumentieren:

| Nr. | Bereich | Ergebnis | Kurze Begründung |
|---|---|---|---|
| 1 | Biometrie | Ja/Nein/Unklar | |
| 2 | Kritische Infrastruktur | Ja/Nein/Unklar | |
| 3 | Bildung/Berufsausbildung | Ja/Nein/Unklar | |
| 4 | Beschäftigung/Arbeit | Ja/Nein/Unklar | |
| 5 | Wesentliche private/öffentliche Dienste | Ja/Nein/Unklar | |
| 6 | Strafverfolgung | Ja/Nein/Unklar | |
| 7 | Migration/Asyl/Grenze | Ja/Nein/Unklar | |
| 8 | Rechtspflege/demokratische Prozesse | Ja/Nein/Unklar | |

### 7. Betreiber- und Governance-Vermerk

Bei allgemeinem Chatbot/GPAI oder offener Zweckverwendung:
- Gibt es KI-Richtlinie?
- Schulung nach Art. 4?
- Rollenrechte und technische Sperren?
- Logging/Audit?
- Freigabeprozess für sensible Use Cases?
- Umgang mit isoliertem Fehlgebrauch?
- Anbieterwerden nach Art. 25 ausgeschlossen?

### 8. Pflichtenprogramm

Nach Ergebnis differenzieren:

**Hochrisiko-Anbieter:** Art. 9 bis 15, Art. 17, Art. 43 bis 49, EU-Datenbank, Post-Market-Monitoring.

**Hochrisiko-Betreiber:** Art. 26, ggf. Art. 27, menschliche Aufsicht, Logs, Eingabedaten, Informationspflichten, Vorfallprozesse.

**Nicht-Hochrisiko:** Art. 50, GPAI, Art. 4 KI-Kompetenz, interne Governance, Datenschutz, Berufsrecht, Re-Evaluation.

**GPAI:** Art. 51 bis 55, Code of Practice, Systemrisiko, technische Dokumentation, Copyright-Policy, Trainingsdaten-Zusammenfassung.

### 9. Normen und Standards

Kurz aufnehmen:
- Gibt es harmonisierte Normen mit Amtsblatt-Fundstelle?
- Werden ISO/IEC 42001, 23894, 22989, 23053 oder Sicherheitsstandards als Orientierung genutzt?
- Welche Standards begründen keine Vermutungswirkung?

### 10. Ergebnisformel

```text
Ergebnis:
Nach den vorliegenden Angaben handelt es sich bei [System] [wahrscheinlich / wahrscheinlich nicht / offen] um ein KI-System nach Art. 3 Nr. 1 KI-VO. [Begründung in 3-5 Sätzen.]

Die Hochrisiko-Einstufung nach Art. 6 Abs. 2 i.V.m. Anhang III ist [wahrscheinlich / nicht ersichtlich / offen], weil [konkreter Zweck und Bereich]. Ein allgemeiner Chatbot/GPAI-Einsatz allein genügt hierfür nicht; entscheidend ist [konkrete Zweckbestimmung/tatsächliche Nutzung].

Die Rückausnahme nach Art. 6 Abs. 3 ist [zu prüfen / greift wahrscheinlich / greift nicht], weil [Profiling/Risiko/Fallgruppe].

Empfohlene nächste Schritte:
1. [Maßnahme]
2. [Maßnahme]
3. [Maßnahme]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Quellenstand und Leitlinienlage sind vor Außenverwendung zu aktualisieren. Keine Rechtsberatung.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
