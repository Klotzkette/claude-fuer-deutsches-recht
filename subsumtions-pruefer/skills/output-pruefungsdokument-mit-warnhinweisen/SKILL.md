---
name: output-pruefungsdokument-mit-warnhinweisen
description: "Erzeugt das vollständige Prüfungsdokument mit Pflicht-Kopfhinweis: kein Rechtsgutachten, kein Rechtsrat, nur mechanische Prüfung anhand Nutzerangaben. Enthaelt alle Warnhinweise an markanten Stellen des Dokuments und Abschluss-Disclaimer im Subsumtions Pruefer."
---

# Output: Prüfungsdokument mit Warnhinweisen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. Wird das Dokument von juristisch nicht vorgebildeten Personen gelesen?
2. Besteht besonderes Haftungsrisiko (Fristen, Vollstreckungshandlungen, Strafrecht)?
3. Soll das Dokument als Grundlage für eine Klageschrift / einen Widerspruch dienen?
4. Sind Generalklauseln oder unbestimmte Rechtsbegriffe einschlägig? → Warnhinweis verschärfen

## Rechtsprechung zur Dokumentationspflicht

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

> **Normwahl-Warnung:** Die nachfolgende Prüfung bezieht sich ausschließlich auf die vom Nutzer genannte Norm. Das System hat keine unabhängige Prüfung vorgenommen, ob diese Norm die einschlägige, vollständige oder richtige Grundlage ist. Die "falsche-Wiese-Warnung" (Skill `falsche-wiese-warnung`) empfiehlt, die Normwahl vorab zu validieren.

### Abschnitt 3 — Tatbestandsmerkmale (je TBM mit Warnhinweis)

Bei jedem Tatbestandsmerkmal, das mit "fraglich" oder "offen" endet:

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

