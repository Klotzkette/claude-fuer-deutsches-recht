---
name: dringlichkeitsmarker-einwilligung-hinweis
description: "Eingehende Mandantenanfrage enthaelt möglicherweise Fristenproblem oder dringenden Handlungsbedarf. Dringlichkeitscheck Kanzlei-Intake. Prüfraster: Signale Hauptverhandlung naechste Woche Kündigungsfrist Zwangsvollstreckung Insolvenzantrag. Dringlichkeitsstufen HOCH (sofortiger Anwalt-Anruf) MITTEL NIEDRIG. Output: Dringlichkeits-Einschaetzung mit konkreter Handlungsempfehlung. Abgrenzung zu anfrage-eingang-parser (Datenextraktion) und erstantwort-generator (Antwort) im Mandantenanfragen Assistent."
---

# Dringlichkeitsmarker

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BRAO § 44 unverzügliche Annahme/Ablehnung, RVG § 34 Erstberatung max. 190 EUR (Verbraucher), DSGVO Art. 13 Information bei Erhebung.
- Tragende Normen verifizieren: BRAO §§ 43a, 44, 49b, BORA §§ 2, 11, BGB §§ 145 ff., 280, 627, 675, GwG §§ 10, 11, RVG §§ 1, 4, 34 (Erstberatung), DSGVO Art. 6, 13 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anfragender (Interessent), Anwalt, Sekretariat, Compliance-Beauftragter, Mandantenbetreuer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Erstkontaktformular, Konfliktscreening, Mandatsvertrag, Vollmacht, Honorarvereinbarung, Mandantendossier, Datenschutzhinweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Dieser Skill erkennt Eile- und Fristen-Signale in der Eingangsanfrage und setzt eine Dringlichkeitsstufe. Bei hoher Dringlichkeit ist ein sofortiger Anwaltsrückruf erforderlich — die anfragende Person darf nicht auf eine E-Mail-Antwort warten.

## Triage zu Beginn
1. Enthält die Anfrage eine konkrete Datumsangabe oder Fristnennung (Gerichtstermin, Kuendigungsfrist, Rechtsmittelfrist)?
2. Welches Rechtsgebiet ist betroffen — welche typischen Fristen gelten (KSchG 3 Wochen, § 517 ZPO 1 Monat Berufung)?
3. Gibt es Anzeichen für Zwangsvollstreckung, Insolvenzantrag oder strafrechtliche Eile?
4. Ist die Dringlichkeitsstufe HOCH — muss der Anwalt sofort anrufen statt auf E-Mail zu warten?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 4 KSchG — Kuendigungsschutzklage-Frist: 3 Wochen ab Zugang der Kuendigung (Notfrist)
- § 517 ZPO — Berufungsfrist: 1 Monat ab Urteilszustellung (Notfrist, unverlaengerbar)
- § 51 BRAO — Haftung: Fristversaeumnis durch mangelnde Dringlichkeits-Erkennung
- § 233 ZPO — Wiedereinsetzung: nur moeglich wenn Kanzlei keine Fahrlässigkeit trifft

## Dringlichkeitsstufen

| Stufe | Kriterium | Konsequenz |
|---|---|---|
| **HOCH** | Konkrete Frist, bevorstehender Termin, Haftungsrisiko | Anwalt ruft sofort zurück; Erstantwort enthält Sofortruf-Hinweis |
| **MITTEL** | Zeitdruck erkennbar, aber keine akute Frist | Rückmeldung innerhalb 24 Stunden |
| **NIEDRIG** | Kein Zeitdruck erkennbar | Normale Bearbeitungsreihenfolge |
| **UNBEKANNT** | Keine Zeitangaben in der Anfrage | Wie MITTEL behandeln |

## Eile-Signale: Explizite Nennungen (HOCH)

### Gerichtstermine und Verhandlungen

- "Hauptverhandlung nächste Woche" / "Termin beim Amtsgericht am [Datum]"
- "einstweilige Verfügung wurde zugestellt"
- "Versäumnisurteil droht" / "ich war nicht bei der Verhandlung"
- "Berufungsfrist läuft ab"
- "Einspruchsfrist gegen den Strafbefehl"

### Vertragsfristen

- "Kündigungsfrist läuft" / "Kündigung zum [Datum]"
- "Vertragsfrist endet diese Woche"
- "Widerspruchsfrist" / "Einspruchsfrist"
- "Rückgabefrist" / "Mängelrüge muss raus"

### Vollstreckung und Insolvenz

- "Zwangsvollstreckung eingeleitet" / "Gerichtsvollzieher war da"
- "Pfändung meines Kontos"
- "Insolvenzantrag wurde gestellt"
- "Pfändungs- und Überweisungsbeschluss erhalten"

### Strafrechtliche Ereignisse

- "bin vorgestern verhaftet worden" / "sitze in Untersuchungshaft"
- "Haftprüfungstermin" / "Haftbefehl"
- "Polizei hat mich heute befragt"
- "Vorladung als Beschuldigter erhalten"

### Behördliche Fristsetzungen

- "Behörde hat mir Frist bis [Datum] gesetzt"
- "Bescheid mit Rechtsmittelfrist erhalten"
- "Widerspruchsfrist gegen Bescheid läuft"
- "Abschiebungsandrohung" / "Ausreisefrist"

## Eile-Signale: Zeitwörter und Adverbien (HOCH oder MITTEL)

| Signal | Stufe |
|---|---|
| "sofort", "dringend", "heute noch", "jetzt" | HOCH |
| "diese Woche", "nächste Woche", "bis Freitag" | HOCH |
| "bald", "in Kürze", "demnächst" | MITTEL |
| "in den nächsten Wochen", "nächsten Monat" | MITTEL |
| "irgendwann", "wenn Sie Zeit haben" | NIEDRIG |

## Haftungsfall-Signale (immer HOCH)

- "Ich werde verklagt" / "mir wurde eine Klage angekündigt"
- "Abmahnung erhalten"
- "Schadensersatzforderung" über einem relevanten Betrag
- "Vertragsstrafe droht"
- "mein Unternehmen ist in Gefahr"

## Hinweis-Text für die Erstantwort-Mail (bei HOCH)

```
WICHTIG: Aus Ihrer Anfrage haben wir entnommen, dass möglicherweise eine
Frist oder ein wichtiger Termin unmittelbar bevorsteht. Bitte rufen Sie
uns umgehend unter [SEKRETARIATS-TELEFON] an. Warten Sie bitte nicht auf
eine Antwort per E-Mail — Fristen können nicht durch eine
Eingangsbestätigung gewahrt werden.
```

## Hinweis für das Sekretariat (Interne Notiz bei HOCH)

```
INTERN — SOFORTMASSNAHME ERFORDERLICH
Rechtsanwalt/Rechtsanwältin muss diese Person sofort zurückrufen.
Mögliche Frist: [Datum/Zeitfenster]
Mögliches Risiko: [Kurzbeschreibung aus dem Signal]
Telefon der anfragenden Person: [aus Parsing]
```

## Falsch-Negativ-Schutz

Bei Unsicherheit über die Dringlichkeit: Eher MITTEL als NIEDRIG. Bei Unsicherheit ob MITTEL oder HOCH: Eher HOCH. Der Schaden durch übersehene Fristen ist größer als der Aufwand eines unnötigen Sofortrückrufs.

## Verweise auf andere Skills

- `anfrage-eingang-parser` — Datenquelle
- `erstantwort-generator` — empfängt die Dringlichkeitsstufe und Hinweis-Texte
- `folgekorrespondenz-vorbereiten` — Dringlichkeitsstufe im CRM-Eintrag
- `mandatsverhaeltnis-hinweis` — bei HOCH: Langform mit Frist-Warnung

---
<!-- AUDIT 27.05.2026 | Bundle 036
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Aktion: Eintrag geloescht.
-->

