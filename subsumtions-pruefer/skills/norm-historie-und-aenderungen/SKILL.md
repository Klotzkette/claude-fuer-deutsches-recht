---
name: norm-historie-und-aenderungen
description: "Für Norm-Historie und Änderungen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix."
---

# Norm-Historie und Änderungen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn — kläre vor der Norm-Historienprüfung

1. Wann hat das relevante Ereignis stattgefunden? (Vertragsschluss, Tatzeitpunkt, Bescheiderlass)
2. Ist die Norm seit dem Ereignis geändert worden oder könnte sie geändert worden sein?
3. Enthält der Sachverhalt eine strafrechtliche Komponente? → § 2 StGB (lex mitior) prüfen
4. Hat der Sachverhalt EU-Bezug? → Anwendungsbeginn und Übergangszeitraum der EU-Verordnung prüfen
5. Gibt es Übergangsvorschriften, die alte Rechtslage für Altfälle erhalten?

## Zentrale Normen zum intertemporalen Recht

- § 2 StGB — lex mitior: Mildestes Gesetz zwischen Tat und Urteil gilt
- Art. 103 Abs. 2 GG — Rückwirkungsverbot im Strafrecht (nulla poena sine lege)
- Art. 20 Abs. 3 GG — Rechtsstaatsprinzip: Vertrauensschutz gegen echte Rückwirkung
- Art. 49 GRCh — Rückwirkungsverbot auf Unionsebene
- Art. 99 KI-VO — gestaffeltes Inkrafttreten (August 2024 - August 2027)

## Prüfungsschritte

### Schritt 1 — Maßgeblicher Zeitpunkt

Das System fragt: Wann hat das relevante Ereignis stattgefunden?

- **Vertragsrecht:** Datum des Vertragsschlusses
- **Deliktsrecht:** Datum der schädigenden Handlung
- **Strafrecht:** Tatzeitpunkt (§ 2 StGB: mildestes Gesetz von Tatzeit bis Urteil — lex mitior)
- **Verwaltungsrecht:** Datum des Bescheiderlasses oder der Widerspruchsentscheidung
- **Steuerrecht:** Veranlagungszeitraum

### Schritt 2 — Normfassung ermitteln

**Entscheidungsbaum:**
```
Liegt das Ereignis vor einer bekannten Normänderung?
├─ Ja → alte Normfassung anwenden (intertemporales Recht)
│ → Übergangsvorschriften prüfen
└─ Nein → aktuelle Normfassung anwenden
 → gesetze-im-internet.de verifizieren
```

Bekannte wichtige Zäsuren:
- Schuldrechtsmodernisierungsgesetz 01.01.2002 (BGB-Schuldrecht)
- DSGVO-Geltungsbeginn 25.05.2018 (Datenschutz)
- KI-VO Inkrafttreten 01.08.2024; Anwendung gestaffelt bis 2027
- Telekommunikationsmodernisierungsgesetz 12.2021 (TKG)

### Schritt 3 — Übergangsvorschriften

- Stichtagsregelungen: Anwendung neuen Rechts ab einem bestimmten Datum
- Bestandsschutzklauseln: Altverträge bleiben unter altem Recht
- Rückwirkungsverbote (Art. 103 Abs. 2 GG im Strafrecht; Art. 20 Abs. 3 GG im Verwaltungsrecht)
- EU-Übergangsrecht: Geltungsbeginn von Verordnungen nach Übergangsfrist

### Schritt 4 — Intertemporales Recht

Das System unterscheidet:
- **Echte Rückwirkung** (belastend): verfassungsrechtlich grundsätzlich verboten
- **Unechte Rückwirkung** (auf laufende Sachverhalte): grundsätzlich zulässig, aber verhältnismäßig
- **Lex mitior im Strafrecht** (§ 2 Abs. 3 StGB): Bei Gesetzesänderung zwischen Tat und Urteil gilt das mildere Gesetz

### Schritt 5 — Hinweis auf Wissensgrenze

Das System gibt in jedem Fall den Hinweis: "Diese Angaben zur Normfassung entsprechen dem Wissensstand des Systems. Für Änderungen danach ist gesetze-im-internet.de oder eur-lex.europa.eu zu prüfen."

## Ausgabe

- Maßgeblicher Zeitpunkt (Nutzerangabe)
- Bekannte Normfassung zu diesem Zeitpunkt
- Wesentliche Änderungen (soweit systembekannt)
- Übergangsvorschriften (soweit einschlägig)
- Empfehlung zur Verifikation der geltenden Fassung

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
