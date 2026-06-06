---
name: beweisbedarf-und-belege-erfassen
description: "Erfasst pro Tatbestandsmerkmal den Beweisbedarf: Beweismittel-Katalog (Urkunden, Zeugen, Sachverständige, Augenschein, Parteivernehmung), Belege hochladen, Tatsachenbehauptung eintragen oder 'beweise ich spaeter'-Markierung setzen. Strukturiertes Beweis-Tracking nach §§ 355-484 ZPO im Subsumtions Pruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Beweisbedarf und Belege erfassen

## Arbeitsbereich

Erfasst pro Tatbestandsmerkmal den Beweisbedarf: Beweismittel-Katalog (Urkunden, Zeugen, Sachverständige, Augenschein, Parteivernehmung), Belege hochladen, Tatsachenbehauptung eintragen oder 'beweise ich spaeter'-Markierung setzen. Strukturiertes Beweis-Tracking nach §§ 355-484 ZPO. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn — kläre vor der Beweiserfassung

1. In welchem Verfahren wird Beweis geführt? (ZPO / VwGO / StPO / SGG / FamFG)
2. Welche Partei trägt die Beweislast für das TBM? (Anspruchsteller oder Gegenseite)
3. Ist die Tatsache streitig — oder unstreitig/offenkundig (§ 291 ZPO)?
4. Liegt bereits ein Beweisbeschluss (§ 359 ZPO) vor?
5. Besteht Gefahr im Verzug? → Antrag auf Sicherung des Beweises §§ 485-494a ZPO prüfen

## Zweck

Jede Subsumtion steht und fällt mit dem Beweisergebnis. Dieser Skill erfasst für jedes Tatbestandsmerkmal (TBM), welche Beweismittel benötigt werden, welche der Nutzer bereits hat und welche noch beschafft werden müssen. Er erstellt eine strukturierte Beweisliste.

## Zentrale Normen

- §§ 355-484 ZPO — Beweisaufnahme allgemein
- § 286 ZPO — Freie Beweiswürdigung; volle richterliche Überzeugung erforderlich
- § 287 ZPO — Schadensschätzung bei Ausschluss anderer Beweismittel
- §§ 415 ff. ZPO — Urkundsbeweis (öffentliche und private Urkunden)
- §§ 373 ff. ZPO — Zeugenbeweis
- §§ 402 ff. ZPO — Sachverständigenbeweis
- §§ 371 ff. ZPO — Augenschein und elektronische Dokumente
- §§ 445-455 ZPO — Parteivernehmung (subsidiär)
- §§ 485-494a ZPO — Selbständiges Beweisverfahren

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Beweismittel-Katalog (ZPO)

| Beweismittel | § ZPO | Typische Nachweise |
|-------------|-------|-------------------|
| Urkundsbeweis | §§ 415 ff. ZPO | Vertrag, Rechnung, E-Mail, Bescheid, Quittung, Protokoll |
| Zeugenbeweis | §§ 373 ff. ZPO | Personen, die den TBM-relevanten Vorgang erlebt haben |
| Sachverständigenbeweis | §§ 402 ff. ZPO | Technische, medizinische, buchhalterische Fragen |
| Augenschein | §§ 371 ff. ZPO | Besichtigung von Sachen, Orten, digitalen Inhalten |
| Parteivernehmung | §§ 445 ff. ZPO | Nur subsidiär; Nutzer als Partei |
| Elektronische Beweismittel | § 371 Abs. 1 S. 2 ZPO | Screenshots, Metadaten, Logs — Echtheit muss dargelegt werden |

Im Verwaltungs- und Strafverfahren gelten die jeweiligen Verfahrensordnungen (VwGO, StPO); das System passt den Katalog an.

## Schritt-für-Schritt-Vorgehen pro TBM

Das System geht jedes TBM der Reihe nach durch und fragt:

1. **Tatsachenbehauptung:** Was behauptet der Nutzer für dieses TBM? (Freitext-Eingabe)
2. **Beweislast:** Wer muss beweisen? — Grundsatz: Wer einen Anspruch geltend macht, trägt die Beweislast für dessen Voraussetzungen; Gegenseite für Einwendungen/Einreden.
3. **Beleg vorhanden?** Der Nutzer kann angeben:
 - (A) Beleg liegt vor (Dokument, Foto, Screenshot) → Hochladen oder Benennen
 - (B) Zeuge bekannt → Name und Erreichbarkeit notieren
 - (C) Tatsache behaupte ich; Beleg beschaffe ich später → Markierung "offen"
 - (D) Keine Tatsache vorhanden für dieses TBM → TBM als nicht erfüllt markieren
4. **Sekundäre Darlegungslast:** Liegt ein Fall vor, in dem der Gegner näherliegende Informationen hat? → Verweis auf BGH-Rechtsprechung zur sekundären Darlegungslast
5. **Beweiswert-Hinweis:** Das System gibt einen groben Hinweis auf den typischen Beweiswert des genannten Beweismittels (z.B. öffentliche Urkunde: voller Beweis § 415 ZPO; Privaturkunde: § 416 ZPO begrenzt).

## Entscheidungsbaum Beweisführung

```
Ist die Tatsache streitig?
├─ Nein → unstreitig oder offenkundig → kein Beweismittel nötig
└─ Ja → Beweislast bestimmen
 ├─ Kläger trägt Last → Beweismittel aus Katalog wählen
 │ ├─ Urkunde verfügbar? → Urkundsbeweis §§ 415 ff. ZPO
 │ ├─ Zeuge vorhanden? → Zeugenbeweis §§ 373 ff. ZPO
 │ ├─ Technische Frage? → Sachverständiger §§ 402 ff. ZPO
 │ └─ Kein direktes Beweismittel? → Anscheinsbeweis prüfen
 └─ Beklagter trägt Last → Einwand/Einrede belegen
```

## Besondere Konstellationen

### Anscheinsbeweis (prima facie)

Bei typischem Geschehensablauf greift der Anscheinsbeweis (z.B. Auffahrunfall → Abstandsmangel). Der Gegner muss den typischen Ablauf erschüttern durch Darlegung atypischer Umstände.

### Elektronische Dokumente

E-Mails, Screenshots und PDFs sind Beweismittel, aber ihre Echtheit kann bestritten werden. Das System empfiehlt:
- Metadaten sichern (Datum, Absender, Header)
- Zeitnahe Sicherung und Archivierung
- Ggf. Datenschutz-Aspekte bei personenbezogenen Drittdaten beachten

### Selbständiges Beweisverfahren (§§ 485-494a ZPO)

Vor Klageerhebung oder wenn Beweis zu sichern ist: Antrag auf Einholung eines Sachverständigengutachtens. Voraussetzung: Antragsteller hat rechtliches Interesse an Feststellung (z.B. drohender Beweismittelverlust, Verjährungsgefahr).

### Zeugenbeweis

Das System fragt nach vollständigem Namen und Adresse des Zeugen. Es weist darauf hin, dass das Gericht den Zeugen selbst lädt.

### Urkundsbeweis — Originale vs. Kopien

Das System weist darauf hin, dass Originale stets vorzuziehen sind. Kopien können bestritten werden (§ 420 ZPO).

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Beweis-Tracking-Liste

Am Ende der Beweiserfassung erstellt das System eine tabellarische Übersicht:

| TBM | Behauptete Tatsache | Beweismittel | Beweislast | Status |
|-----|--------------------|--------------|-----------|----|
| [TBM 1] | [Nutzerangabe] | [Typ] | Kläger/Beklagter | vorhanden / offen / fehlt |
| [TBM 2] | … | … | … | … |

"Offen" markierte TBM werden als Risikopositionen der Klage / des Antrags ausgewiesen.

## Output-Template Beweisliste (Mandantenbrief-Auszug)

**Adressat:** Mandant — Tonfall verständlich-erklärend

```
Sehr geehrte/r Frau/Herr [NAME],

zur Vorbereitung des Verfahrens [AKTENZEICHEN] benötige ich folgende
Unterlagen und Informationen:

1. [Beweismittel zu TBM 1] — bitte bis [DATUM] einreichen
2. [Zeuge zu TBM 2] — Name und Anschrift: [...]
3. [Noch offen / wird durch Gegenseite beizubringen]

Bitte beachten Sie: Ohne diese Nachweise kann ich den Anspruch auf
[RECHTSVERLETZUNG] nicht mit der erforderlichen Sicherheit belegen.

Mit freundlichen Grüßen
[KANZLEI]
```

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.

<!-- AUDIT 27.05.2026
BGH VI ZR 290/18 (NOT_FOUND): Aktenzeichen existiert auf dejure.org nicht. Gesamte Zeile aus "Aktuelle Rechtsprechung" entfernt.
-->
