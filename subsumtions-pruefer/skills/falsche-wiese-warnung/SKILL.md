---
name: falsche-wiese-warnung
description: "Warnt vor typischen Falschverortungen im Recht: Vertrag statt Delikt, Verwaltungsakt vs. Realakt, Strafrecht statt Ordnungswidrigkeit, Unionsrecht statt nationales Recht. Mechanisches Durchprüfen der richtigen Prüfungsebene vor Normanwendung im Subsumtions Pruefer: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Falsche-Wiese-Warnung

## Arbeitsbereich

Warnt vor typischen Falschverortungen im Recht: Vertrag statt Delikt, Verwaltungsakt vs. Realakt, Strafrecht statt Ordnungswidrigkeit, Unionsrecht statt nationales Recht. Mechanisches Durchprüfen der richtigen Prüfungsebene vor Normanwendung. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn — kläre vor der Normwahl

1. Beschreibe den Sachverhalt in einem Satz: Wer will was von wem woraus?
2. Gibt es eine Willenseinigung (Vertrag) oder eine einseitige Handlung?
3. Ist eine Behörde oder staatliche Stelle beteiligt? → öffentliches Recht prüfen
4. Sind Strafbehörden involviert oder droht eine Strafverfolgung?
5. Hat der Sachverhalt einen EU-Bezug? → Anwendungsvorrang Unionsrecht prüfen

## Zweck

"Auf der falschen Wiese grasen" ist ein klassisches Problem der Rechtsanwendung: Man prüft eine Norm sorgfältig und korrekt — aber die falsche Norm. Dieser Skill kann auf typische Muster hinweisen und Nutzereingaben einer Plausibilitätskontrolle unterziehen.

Dieser Skill wird automatisch oder auf Anforderung aktiviert, wenn der Sachverhalt oder die gewählte Norm Anzeichen einer Fehlverortung enthält.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen zur Einordnung

- § 35 VwVfG — Definition Verwaltungsakt (Regelung, Einzelfall, Außenwirkung)
- § 40 VwGO — Eröffnung des Verwaltungsrechtswegs (öffentlich-rechtliche Streitigkeit)
- § 13 GVG — Eröffnung des ordentlichen Rechtswegs (bürgerliche Rechtsstreitigkeiten)
- § 21 OWiG — Tateinheit von Straftat und Ordnungswidrigkeit (Straftat geht vor)
- Art. 288 AEUV — Unmittelbare Geltung von EU-Verordnungen

## Typische Falschverortungen

### 1. Vertrag statt Delikt (oder umgekehrt)

**Muster:** Nutzer prüft Vertragsrecht (§§ 280 ff. BGB), obwohl kein Vertrag besteht. Oder: Nutzer prüft § 823 Abs. 1 BGB, obwohl eine vertragliche Sonderbeziehung vorliegt.

**Indizien für Fehlverortung:** Keine Willenserklärungen beschrieben; kein Vertragsschluss erwähnt; Handlung ist einseitig schädigend ohne Vertragsbezug.

**Hinweis des Systems:** "Ihr Sachverhalt enthält keinen erkennbaren Vertragsschluss. Bitte prüfen Sie, ob eine deliktische Anspruchsgrundlage (§ 823 Abs. 1 oder Abs. 2 BGB, § 826 BGB) primär einschlägig ist."

### 2. Verwaltungsakt statt Realakt

**Muster:** Nutzer möchte ein staatliches Handeln anfechten, das kein Verwaltungsakt ist (z.B. staatliche Warnung, schlicht-hoheitliches Handeln).

**Indizien:** Kein Regelungscharakter beschrieben; keine Einzelfallentscheidung; keine Rechtsbehelfsbelehrung im Bescheid.

**Entscheidungsbaum:**
```
Hat das staatliche Handeln Regelungscharakter (§ 35 VwVfG)?
├─ Ja → Verwaltungsakt → Anfechtungsklage § 42 VwGO
└─ Nein → Realakt → allg. Leistungsklage/Unterlassungsklage § 40 VwGO
```

### 3. Strafrecht statt Ordnungswidrigkeit (oder umgekehrt)

**Muster:** Nutzer prüft § 303 StGB (Sachbeschädigung), obwohl es sich um eine Ordnungswidrigkeit nach OWiG handeln könnte.

**Hinweis des Systems:** "Prüfen Sie zunächst, ob der Sachverhalt eine Ordnungswidrigkeit nach dem OWiG oder einem Nebengesetz erfüllt. Tateinheit: § 21 OWiG — Strafrecht geht OWiG vor."

### 4. Unionsrecht statt nationales Recht (oder umgekehrt)

**Muster:** Nutzer prüft nationales Datenschutzgesetz (BDSG), obwohl die DSGVO als EU-Verordnung unmittelbar gilt.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 5. Weitere typische Muster

- Schadensersatz statt Unterlassung (und umgekehrt) — § 1004 BGB bei Dauerstörung
- Primäranspruch statt Sekundäranspruch (Erfüllung statt Schadensersatz statt der Leistung)
- WEG-Recht statt BGB-Schuldrecht bei Eigentumswohnungen (WEG seit 01.12.2020 reformiert)
- Erbrecht statt Familienrecht bei Güterstand-Fragen
- Insolvenzrecht als Vorfrage bei Ansprüchen gegen insolvente Schuldner

## Ausgabe

Das System gibt strukturierten Hinweis:
- Erkanntes Muster der Fehlverortung
- Empfohlene Alternativnorm oder -rechtsgebiet
- Frage an den Nutzer: Möchten Sie die alternative Norm prüfen?

Das System setzt die Prüfung der ursprünglich gewählten Norm nur auf ausdrücklichen Nutzerwunsch fort.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
