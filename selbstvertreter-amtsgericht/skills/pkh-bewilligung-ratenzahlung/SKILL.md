---
name: pkh-bewilligung-ratenzahlung
description: "PKH Bewilligung Ratenzahlung im Selbstvertretung am Amtsgericht: prüft konkret Folgen der PKH-Entscheidung Bewilligung mit oder ohne Raten, Ratenzahlung bei PKH-Bewilligung nach § 120 ZPO, Antrag auf Prozesskostenhilfe nach § 114 ZPO. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# PKH Bewilligung Ratenzahlung

## Arbeitsbereich

**PKH Bewilligung Ratenzahlung** ordnet den Fall über die tragenden Prüfungslinien: Folgen der PKH-Entscheidung Bewilligung mit oder ohne Raten, Ratenzahlung bei PKH-Bewilligung nach § 120 ZPO, Antrag auf Prozesskostenhilfe nach § 114 ZPO. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `pkh-bewilligung-ablehnung-folgen` | Folgen der PKH-Entscheidung Bewilligung mit oder ohne Raten Beiordnung Anwalt Ablehnung wegen fehlender Erfolgsaussicht Bedürftigkeit oder Mutwilligkeit. Beschwerde gegen ablehnenden PKH-Beschluss nach § 127 ZPO und sofortige Beschwerde. |
| `pkh-ratenzahlung-bewilligung` | Ratenzahlung bei PKH-Bewilligung nach § 120 ZPO. Berechnung der monatlichen Rate nach einsetzbarem Einkommen Tabelle § 115 II ZPO. Maximale Laufzeit 48 Monate Aenderung Anpassung und vorzeitige Tilgung. Wirkung auf Gerichts- und Anwaltskosten. |
| `prozesskostenhilfe-pkh-114-zpo` | Antrag auf Prozesskostenhilfe nach § 114 ZPO. Voraussetzungen Bedürftigkeit Erfolgsaussicht keine Mutwilligkeit. Antragsformular Belege Einkommensnachweise. Wirkung Befreiung von Gerichtskosten und Anwaltskosten. Hinweise für Selbstvertreter. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: ZPO §§ 78, 79, 129, 253, 495a, 511, 517, GVG §§ 23, 71, SGG §§ 73, 78, 87, 90, 144, 160; §23 GVG; §511 ZPO-Grenzen, Klage — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `pkh-bewilligung-ablehnung-folgen`

**Fokus:** Folgen der PKH-Entscheidung Bewilligung mit oder ohne Raten Beiordnung Anwalt Ablehnung wegen fehlender Erfolgsaussicht Bedürftigkeit oder Mutwilligkeit. Beschwerde gegen ablehnenden PKH-Beschluss nach § 127 ZPO und sofortige Beschwerde.

# Wenn PKH bewilligt oder abgelehnt wird

## Worum geht es?

Nach Ihrem PKH-Antrag entscheidet das Gericht durch Beschluss. Wenn bewilligt, koennen Sie ohne (oder mit reduzierten) Kosten klagen. Wenn abgelehnt: Sie tragen die Kosten selbst oder koennen die Beschwerde einlegen. Diese Skill erklaert, was die Bewilligung praktisch heisst und was Sie bei Ablehnung tun koennen.

## Wann brauchen Sie diese Skill?

- Sie haben PKH beantragt und auf Antwort warten.
- Sie haben einen PKH-Beschluss bekommen.
- Sie wurden abgelehnt und wollen Beschwerde pruefen.

## Fachbegriffe (kurz erklaert)

- **PKH-Beschluss**: Schriftliche Entscheidung des Gerichts ueber den PKH-Antrag.
- **Beiordnung**: Zuweisung eines konkreten Anwalts auf Staatskosten.
- **Sofortige Beschwerde**: Rechtsmittel gegen bestimmte Beschluesse (§ 127 II ZPO).

## Rechtsgrundlagen

- **§ 119 ZPO** — Form und Wirkung des Bewilligungs-Beschlusses.
- **§ 120 ZPO** — Ratenzahlung.
- **§ 121 ZPO** — Beiordnung eines Anwalts.
- **§ 124 ZPO** — Aufhebung der Bewilligung.
- **§ 127 ZPO** — Sofortige Beschwerde.

## Schritt-für-Schritt-Anleitung

### Schritt 1 — Beschluss lesen

Der PKH-Beschluss enthaelt:

- Bewilligung oder Ablehnung.
- Bei Bewilligung: ohne Raten oder mit Raten.
- Bei Bewilligung: ggf. Beiordnung eines Anwalts.
- Bei Ablehnung: Begruendung.

### Schritt 2 — Bewilligung ohne Raten

- Sie zahlen keinen Vorschuss.
- Gerichtskosten traegt im Verfahren der Staat.
- Anwalt (wenn beigeordnet) bekommt Gebuehr vom Staat.
- **Achtung**: Bei Niederlage zahlen Sie die Kosten der Gegenseite trotzdem.

### Schritt 3 — Bewilligung mit Raten

- Sie zahlen monatliche Raten an die Gerichtskasse.
- Hoehe richtet sich nach Ihrer Einkommens-Lage (Tabelle § 115 II ZPO).
- Bis zu 48 Monaten.

Skill `pkh-ratenzahlung-bewilligung`.

### Schritt 4 — Beiordnung Anwalt

§ 121 II ZPO: Wenn die Sache nicht einfach gelagert ist und Sie nicht selbst vertreten koennen, wird Anwalt beigeordnet. Bei AG ist Anwaltszwang nicht zwingend — Beiordnung also nicht zwingend.

Wenn Sie einen bestimmten Anwalt wollen: Beiordnung beantragen unter Nennung des Namens. Anwalt muss zustimmen.

### Schritt 5 — Ablehnung: Begruendung lesen

Haeufige Ablehnungsgruende:

- **Keine Erfolgsaussicht**: Das Gericht haelt Ihre Klage für aussichtslos.
- **Nicht-Beduerftigkeit**: Ihr Einkommen ist zu hoch.
- **Mutwilligkeit**: Die Klage wuerde ein verstaendiger nicht-PKH-Beduerftiger nicht erheben.

### Schritt 6 — Beschwerde gegen Ablehnung

§ 127 II ZPO: Sofortige Beschwerde innerhalb von **2 Wochen** ab Zustellung des Beschlusses.

Form: Schriftsatz oder zu Protokoll. Begruendung warum die Ablehnung unzutreffend ist.

Beschwerdegericht: LG (bei AG-Beschluessen) oder OLG (bei LG-Beschluessen).

### Schritt 7 — Bei nicht-Erfolgsaussicht: Vortrag verbessern

Wenn das Gericht meint, Ihre Klage habe keine Erfolgsaussicht, lesen Sie die Begruendung genau:

- Vielleicht haben Sie Beweis nicht klar benannt.
- Vielleicht fehlt Sachverhalts-Vortrag.
- Vielleicht ist Anspruchsgrundlage nicht klar.

Ergaenzungs-Schriftsatz mit klarstellenden Vortrag und Beweis nachreichen. Manchmal ueberdenkt das Gericht von Amts wegen.

### Schritt 8 — Wenn Beschwerde scheitert

Sie tragen die Kosten selbst. Sie koennen trotzdem klagen — aber dann mit vollem Risiko.

Alternativen:

- Anders / kuerzer klagen (Teilklage, niedrigerer Streitwert).
- Aussergerichtliche Loesung (Mediation, Vergleich).
- Verzicht — wenn Risiko zu hoch.

### Schritt 9 — Aufhebung der Bewilligung

§ 124 ZPO: Bewilligung kann aufgehoben werden, wenn:

- Falsche Angaben gemacht wurden.
- Einkommens-Verbesserung tritt ein (§ 120a Mitteilungs-Pflicht).
- Klage aussichtslos wurde.

Folge: Sie zahlen rueckwirkend.

## Worauf Sie besonders achten muessen

- **Beschwerde-Frist 2 Wochen**: Pflicht.
- **Aenderungs-Meldung § 120a**: Wenn sich Einkommen erheblich aendert.
- **PKH heilt nicht Gegnerkosten**: Bei Niederlage zahlen Sie diese trotzdem.

## Typische Fehler

- "Beschluss kommt automatisch zur Beratungshilfe." → Nein, separate Antraege.
- "Bei PKH bin ich gegen alle Kosten geschuetzt." → Nur eigene Kosten.
- "Beschwerde-Frist 1 Monat." → 2 Wochen!

## Querverweise

- `prozesskostenhilfe-pkh-114-zpo` — Grundantrag.
- `pkh-ratenzahlung-bewilligung` — Raten.
- `beratungshilfe-aussergerichtlich-brh` — Beratungshilfe.
- `kostenrisiko-streitwert-berechnen-gkg` — Kosten.
- `wann-doch-anwalt-grenzfaelle` — Anwalt.

## Quellen und Aktualitaet

Stand: 05/2026. §§ 119 ff. ZPO unveraendert.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `pkh-ratenzahlung-bewilligung`

**Fokus:** Ratenzahlung bei PKH-Bewilligung nach § 120 ZPO. Berechnung der monatlichen Rate nach einsetzbarem Einkommen Tabelle § 115 II ZPO. Maximale Laufzeit 48 Monate Aenderung Anpassung und vorzeitige Tilgung. Wirkung auf Gerichts- und Anwaltskosten.

# PKH mit Ratenzahlung

## Worum geht es?

Wer ein einsetzbares Einkommen hat, das aber nicht hoch genug für Selbstzahlung ist, bekommt PKH mit Ratenzahlung. Das Gericht setzt eine monatliche Rate fest, die Sie an die Gerichtskasse zahlen. Bis maximal 48 Monate. Diese Skill zeigt, wie die Rate berechnet wird und was Sie tun koennen, wenn sich die Einkommens-Lage aendert.

## Wann brauchen Sie diese Skill?

- Sie haben PKH mit Raten bewilligt bekommen.
- Sie wollen vorhersagen, was die Raten kosten koennten.
- Sie haben Einkommens-Aenderung.

## Fachbegriffe (kurz erklaert)

- **Einsetzbares Einkommen**: Einkommen nach Abzug der Freibetraege.
- **Ratenzahlung**: Monatliche Zahlung an Gerichtskasse.
- **Tabelle § 115 II ZPO**: Rechtsverordnung mit Raten-Stufen je Einkommen.

## Rechtsgrundlagen

- **§ 115 ZPO** — Einkommensgrenze.
- **§ 115 II ZPO** — Raten-Tabelle (Verordnung).
- **§ 120 ZPO** — Ratenzahlung; max 48 Monate.
- **§ 120a ZPO** — Mitteilungs-Pflicht.

## Schritt-für-Schritt-Anleitung

### Schritt 1 — Einsetzbares Einkommen berechnen

Brutto-Einkommen — Steuer — SV-Beitraege = Netto.

Netto — Freibetrag für Partei + Partner + Kinder — Mietkosten — Versicherung-Beitrag = Einsetzbares Einkommen.

### Schritt 2 — Rate ablesen

Tabelle § 115 II ZPO (gerundete Hoehen — aktuelle Tabelle verifizieren):

- Einsetzbares Einkommen 0 EUR: Rate 0 EUR (PKH ohne Raten).
- Einsetzbares Einkommen 1-50 EUR: Rate 15 EUR.
- Einsetzbares Einkommen 51-100 EUR: Rate 30 EUR.
- ... usw. bis Maximum.

Aktuelle Tabelle verifizieren ueber justiz.de oder PKH-Rechner.

### Schritt 3 — Laufzeit

§ 120 III ZPO: Maximal 48 Monatsraten. Wenn die Summe nach 48 Raten die Verfahrenskosten erreicht hat: ggf. weniger Raten.

Wenn Verfahrenskosten frueher abgedeckt: Raten enden frueher.

### Schritt 4 — Zahlweise

- Sie zahlen monatlich an die Gerichtskasse.
- IBAN und Aktenzeichen wie ueblich.
- Daueraufrag empfehlenswert (vergessens-Risiko).

### Schritt 5 — Aenderung der Einkommens-Lage

§ 120a ZPO: Wenn sich Ihre Einkommens-/Vermoegens-Lage **erheblich** aendert, muessen Sie das melden.

- Einkommens-**Verbesserung**: Rate wird ggf. erhoeht.
- Einkommens-**Verschlechterung**: Auf Antrag Rate verringert oder ausgesetzt.

Aenderungs-Schwelle: BGH-Rechtsprechung 100 EUR pro Monat.

### Schritt 6 — Bei Niederlage

Auch bei PKH mit Raten zahlen Sie die Kosten der Gegenseite, wenn Sie verlieren. Die Raten gehen weiter — und Gegenseiten-Kosten kommen oben drauf.

### Schritt 7 — Bei Erfolg

Wenn Sie gewinnen, traegt der Beklagte die Kosten. Sie bekommen ggf. Ihren Ratenanteil zurueck.

### Schritt 8 — Vorzeitige Tilgung

Sie koennen die Raten vorzeitig komplett zahlen — entlastet Sie laufend.

## Worauf Sie besonders achten muessen

- **Meldepflicht**: Wenn Sie Einkommens-Aenderung nicht melden, kann PKH rueckwirkend aufgehoben werden (§ 124 ZPO).
- **Tabelle aktualisieren**: Verifizieren Sie die aktuelle PKH-Tabelle.
- **Vorlage-Pflicht**: Vier-jaehrliche Nachpruefung kann Belege anfordern.

## Typische Fehler

- "Raten gelten lebenslang." → Maximal 48 Monate.
- "Bei Lohnerhoehung muss ich nichts melden." → Doch — § 120a Mitteilungs-Pflicht.
- "PKH-Rate ist Lohnpfaendung." → Nein, freiwillige Zahlung — aber Sie verlieren PKH, wenn Sie nicht zahlen.

## Querverweise

- `prozesskostenhilfe-pkh-114-zpo` — Grundantrag.
- `pkh-bewilligung-ablehnung-folgen` — Folgen.
- `beratungshilfe-aussergerichtlich-brh` — Beratungshilfe.
- `kostenrisiko-streitwert-berechnen-gkg` — Kosten.

## Quellen und Aktualitaet

Stand: 05/2026. § 120 ZPO unveraendert. Aktuelle PKH-Raten-Tabelle ueber justiz.de verifizieren.

## 3. `prozesskostenhilfe-pkh-114-zpo`

**Fokus:** Antrag auf Prozesskostenhilfe nach § 114 ZPO. Voraussetzungen Bedürftigkeit Erfolgsaussicht keine Mutwilligkeit. Antragsformular Belege Einkommensnachweise. Wirkung Befreiung von Gerichtskosten und Anwaltskosten. Hinweise für Selbstvertreter.

# Prozesskostenhilfe (PKH): Klage trotz Geldknappheit

## Worum geht es?

Wenn Sie sich Klage und Gerichtskosten nicht leisten koennen, gibt es **Prozesskostenhilfe (PKH)** nach §§ 114 ff. ZPO. Der Staat uebernimmt dann ganz oder teilweise die Gerichtskosten und ggf. die Anwaltskosten. PKH wird auf Antrag gewaehrt und an drei Voraussetzungen geknuepft: Sie sind beduerftig, die Klage hat hinreichende Erfolgsaussicht, sie ist nicht mutwillig.

## Wann brauchen Sie diese Skill?

- Sie wollen klagen, koennen den Vorschuss aber nicht zahlen.
- Sie wurden verklagt und brauchen Verteidigungs-Hilfe.
- Sie wollen die Voraussetzungen pruefen.

## Fachbegriffe (kurz erklaert)

- **Prozesskostenhilfe (PKH)**: Sozialleistung im Zivilprozess, die Gerichts- und Anwaltskosten ganz oder teilweise traegt.
- **Beduerftigkeit**: Wirtschaftliche Lage, in der Sie die Kosten nicht oder nur teilweise aufbringen koennen.
- **Erfolgsaussicht**: Wenn die Klage bei summarischer Pruefung berechtigt erscheint.
- **Mutwilligkeit**: Klage, die ein verstaendiger nicht-PKH-Beduerftiger nicht erheben wuerde.

## Rechtsgrundlagen

- **§ 114 I ZPO** — Voraussetzungen PKH.
- **§ 115 ZPO** — Einkommen, einzusetzendes Vermoegen.
- **§ 117 ZPO** — Antragsform.
- **§ 118 ZPO** — Anhörung Gegner.
- **§ 120 ZPO** — Ratenzahlung.
- **§ 121 ZPO** — Beiordnung eines Anwalts.
- **§ 124 ZPO** — Aufhebung der Bewilligung.

## Schritt-für-Schritt-Anleitung

### Schritt 1 — Voraussetzungen pruefen

Drei Bedingungen muessen erfuellt sein (§ 114 I ZPO):

1. **Beduerftigkeit**: Sie koennen die Kosten nicht oder nur in Raten aufbringen.
2. **Erfolgsaussicht**: Ihre Klage hat bei summarischer Pruefung Aussicht auf Erfolg.
3. **Keine Mutwilligkeit**: Eine vermoegende Partei wuerde die Klage gleichermassen erheben.

Wenn ein Punkt fehlt, scheitert PKH.

### Schritt 2 — Beduerftigkeit berechnen

§ 115 ZPO regelt Einkommens-Anrechnung:

- Nettoeinkommen (Lohn, Selbstaendigkeit, Sozialleistungen).
- Minus Freibetraege für Sie selbst, Partner, Kinder.
- Minus Mietkosten in angemessener Hoehe.
- Minus weitere Abzuege (Versicherungen, Werbungskosten).

= Einsetzbares Einkommen. Wenn das Ergebnis null oder negativ: PKH ohne Raten.

Wenn positiv: PKH mit Ratenzahlung.

Faustregel (sehr grob): Wer Buergergeld bekommt, kriegt PKH ohne Raten. Mit mittlerem Einkommen Ratenzahlung. Mit hoeherem Einkommen kein PKH.

### Schritt 3 — Vermoegen anrechnen

§ 115 III ZPO: Schonvermoegen. Auto, Hausrat, kleines Sparbuch bleiben.

Wenn Sie groesseres Bargeld, Wertpapiere, Immobilie haben: Anrechnung. Sie muessen das einsetzen, bevor PKH.

### Schritt 4 — Antragsformular

Das amtliche Formular "Erklaerung ueber die persönlichen und wirtschaftlichen Verhaeltnisse" ist Pflicht. Verfuegbar online und in der Rechtsantragsstelle. Sie fuellen aus:

- Persoenliche Daten.
- Familienstand, Unterhaltspflichten.
- Einkommen aller Art.
- Vermoegen.
- Mietkosten und sonstige laufende Kosten.

### Schritt 5 — Belege

Anzufuegen:

- Letzte 3 Lohnabrechnungen (oder Buergergeld-Bescheid).
- Mietvertrag mit aktueller Miete.
- Kontoausziuege (letzte 3 Monate).
- Versicherungs-Beitragsnachweise.
- Bei Selbstaendigen: Steuerbescheid und betriebswirtschaftliche Auswertung.

### Schritt 6 — Antrag einreichen

Variante A: PKH-Antrag **zusammen mit der Klage** einreichen.

Variante B: Vorab PKH-Antrag (z. B. wenn Sie nur klaeren wollen, ob PKH bewilligt wird, bevor Sie Klage einreichen).

Bei Selbstvertretung Sie reichen ein:

- Klage-Entwurf (auch wenn Sie sie noch nicht "richtig" eingereicht haben).
- PKH-Antrag mit Belegen.

### Schritt 7 — Pruefung und Entscheidung

Gericht prueft:

- Erfolgsaussicht: kurze summarische Pruefung.
- Beduerftigkeit: Belege.
- Mutwilligkeit: nur in seltenen Faellen relevant.

Entscheidung per Beschluss (= keine muendliche Verhandlung).

### Schritt 8 — Wenn bewilligt

- Sie zahlen keinen oder reduzierten Vorschuss.
- Bei Beiordnung eines Anwalts (§ 121 ZPO): Anwalt bekommt seine Gebuehr vom Staat.
- Bei Niederlage: Sie tragen die Kosten der Gegenseite trotzdem (PKH deckt nur **Ihre** Kosten ab) — § 123 ZPO.

### Schritt 9 — Anwaltsbeiordnung pruefen

Auch wenn vor AG kein Anwaltszwang besteht, kann Anwalt beigeordnet werden (§ 121 II ZPO), wenn:

- "Sache nicht einfach gelagert ist" und
- Sie nicht in der Lage sind, sich selbst zu vertreten.

In Praxis selten bewilligt — meist nur bei komplexen Faellen.

## Worauf Sie besonders achten muessen

- **Belege vollstaendig**: Unvollstaendige Antraege werden zurueckgewiesen.
- **Wahrheitspflicht** beim PKH-Antrag — falsche Angaben sind Betrug.
- **PKH deckt nur Ihre Kosten**: Bei Niederlage zahlen Sie Gegnerkosten.
- **Aenderung der Einkommens-Situation** muss gemeldet werden (§ 120a ZPO).

## Typische Fehler

- "PKH heisst, ich habe nichts zu zahlen." → Bei mittlerem Einkommen Raten.
- "PKH deckt auch Gegnerkosten." → Nein, nur eigene Kosten.
- "Ich beantrage PKH nach Klage-Einreichung." → Geht, aber besser gleichzeitig.

## Querverweise

- `kostenrisiko-streitwert-berechnen-gkg` — Kosten ueberhaupt.
- `pkh-bewilligung-ablehnung-folgen` — Wenn abgelehnt.
- `pkh-ratenzahlung-bewilligung` — Raten.
- `beratungshilfe-aussergerichtlich-brh` — Vor Prozess.
- `gerichtskostenvorschuss-12-gkg` — Vorschuss.

## Quellen und Aktualitaet

Stand: 05/2026. §§ 114 ff. ZPO unveraendert. PKH-Freibetraege jaehrlich angepasst — aktuelle Hoehen ueber Justizportal verifizieren.
