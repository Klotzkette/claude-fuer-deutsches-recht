---
name: output-pruefungsdokument-mit-warnhinweisen
description: "Erzeugt das vollstaendige Pruefungsdokument mit Pflicht-Kopfhinweis: kein Rechtsgutachten, kein Rechtsrat, nur mechanische Pruefung anhand Nutzerangaben. Enthaelt alle Warnhinweise an markanten Stellen des Dokuments und Abschluss-Disclaimer."
---

# Output: Prüfungsdokument mit Warnhinweisen

## Zweck

Dieses Ausgabe-Format ist das vollständigste und transparenteste Format des Subsumtions-Prüfers. Es enthält an jedem kritischen Punkt des Dokuments einen Warnhinweis, der dem Leser klar macht, was das Dokument ist — und was es ausdrücklich nicht ist.

## Triage zu Beginn

1. Wird das Dokument von juristisch nicht vorgebildeten Personen gelesen?
2. Besteht besonderes Haftungsrisiko (Fristen, Vollstreckungshandlungen, Strafrecht)?
3. Soll das Dokument als Grundlage für eine Klageschrift / einen Widerspruch dienen?
4. Sind Generalklauseln oder unbestimmte Rechtsbegriffe einschlägig? → Warnhinweis verschärfen

## Rechtsprechung zur Dokumentationspflicht

- BGH, Urt. v. 15.04.2021 - IX ZR 143/20, NJW 2021, 1740 — Anwälte müssen ihre Beratungsleistung dokumentieren; unzureichende Dokumentation gefährdet den Nachweis der Pflichterfüllung im Haftungsfall.
- BGH, Urt. v. 07.03.2019 - IX ZR 221/18, NJW 2019, 2020 — Fehlen Warnhinweise zu drohenden Fristen im Beratungsdokument, verletzt der Berater seine Pflicht.
- BGH, Urt. v. 23.05.2019 - IX ZR 143/18, NJW 2019, 2296 — Eine mechanisch erzeugte Prüfung ersetzt niemals die persönliche anwaltliche Haftung; der Anwalt haftet für Fehler auch dann, wenn er sich auf ein externes Hilfsmittel gestützt hat.
- BVerfG, Beschl. v. 26.01.2021 - 1 BvR 2187/18, NJW 2021, 1022 — Das Recht auf effektiven Rechtsschutz (§ 19 Abs. 4 GG) setzt voraus, dass Betroffene ihre Rechtslage korrekt einschätzen können; irreführende Rechtsdokumente können dieses Recht verletzen.

## Pflicht-Kopf (jedes Prüfungsdokument beginnt damit)

```
============================================================
PRÜFUNGSDOKUMENT — KEINE RECHTSBERATUNG
============================================================

Dieses Dokument ist keine Rechtsberatung und keine
Rechtsanwendung. Es prüft mechanisch eine vom Nutzer
behauptete Norm anhand vom Nutzer behaupteter Tatsachen.

Das System kann nicht prüfen:
• ob der Nutzer die richtige Norm gewählt hat
• ob der Sachverhalt vollständig oder korrekt geschildert ist
• ob es eine vorrangige, speziellere oder günstigere Norm gibt
• ob die Gegenseite andere Tatsachen behauptet oder belegt
• ob Generalklauseln und unbestimmte Rechtsbegriffe im
  Einzelfall wie ausgelegt zugunsten oder zulasten des Nutzers
  ausgelegt werden
• ob das Prüfungsergebnis vor Gericht standhält

Erstellt: [Datum]
Betreff: Mechanische Subsumtionsprüfung
Norm: [geprüfte Norm]
Sachverhalt: [kurze Zusammenfassung Nutzerangabe]
============================================================
```

## Struktur des Gesamtdokuments

### Abschnitt 1 — Eingabe (Nutzereingaben dokumentiert)

Alle Nutzerangaben werden wortwörtlich wiedergegeben. Keine Ergänzungen durch das System. Damit ist für den Leser klar, worauf das Prüfungsergebnis beruht.

### Abschnitt 2 — Normwahl (mit Warnhinweis)

> **Normwahl-Warnung:** Die nachfolgende Prüfung bezieht sich ausschließlich auf die vom Nutzer genannte Norm. Das System hat keine unabhängige Prüfung vorgenommen, ob diese Norm die einschlägige, vollständige oder richtige Grundlage ist. Die „falsche-Wiese-Warnung" (Skill `falsche-wiese-warnung`) empfiehlt, die Normwahl vorab zu validieren.

### Abschnitt 3 — Tatbestandsmerkmale (je TBM mit Warnhinweis)

Bei jedem Tatbestandsmerkmal, das mit „fraglich" oder „offen" endet:

> **TBM-Warnhinweis:** Dieses Tatbestandsmerkmal konnte nicht abschließend beurteilt werden. Das Gesamtergebnis ist entsprechend unsicher.

### Abschnitt 4 — Generalklauseln und unbestimmte Rechtsbegriffe (mit Warnhinweis)

> **Generalklausel-Warnung:** Das Prüfungsergebnis zu diesem Merkmal ist eine Indiziensammlung, kein Subsumtionsergebnis. Generalklauseln und unbestimmte Rechtsbegriffe können mechanisch nicht abschließend beurteilt werden.

### Abschnitt 5 — Subsumtionsergebnis (mit Warnhinweis)

> **Ergebnis-Warnung:** Das nachfolgende Ergebnis gilt nur unter der Prämisse, dass alle Nutzerangaben vollständig und korrekt sind und die gewählte Norm die einschlägige Grundlage ist. Abweichende Tatsachen oder eine andere Normwahl würden zu einem anderen Ergebnis führen.

### Abschnitt 6 — Abschluss-Disclaimer (Pflicht)

```
============================================================
ABSCHLUSS-DISCLAIMER
============================================================

Dieses Prüfungsdokument wurde automatisch auf Basis der
Eingaben des Nutzers erstellt. Es ist kein Rechtsgutachten,
keine anwaltliche Stellungnahme und keine Rechtsberatung.

Für alle rechtlich relevanten Entscheidungen — insbesondere
Klageerhebung, Widerspruch, Strafanzeige, Vertragsschluss
oder -kündigung — ist die Prüfung durch einen zugelassenen
Rechtsanwalt (ggf. Fachanwalt) unerlässlich.

Falsche Normwahl oder falsche Sachverhaltsdarstellung kann
das gesamte Ergebnis entwerten.
============================================================
```

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.
