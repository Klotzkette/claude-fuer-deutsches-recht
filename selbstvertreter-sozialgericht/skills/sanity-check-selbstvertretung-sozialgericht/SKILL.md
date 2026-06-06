---
name: sanity-check-selbstvertretung-sozialgericht
description: "Letzter Sanity-Check vor Widerspruch, Klage, Eilantrag, Stellungnahme, Termin oder Berufung im Sozialgerichtsverfahren. Prüft Frist, Bescheidkette, richtige Klageart, Eilbedürftigkeit, Belege, medizinische Unterlagen, Antrag, Kostenfreiheit, PKH und rote Flaggen."
---

# Sanity-Check Selbstvertretung Sozialgericht

## Fachlicher Anker

- **Normen:** § 7, § 7a, §§ 20.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Zweck

Dieser Skill prüft, ob ein Widerspruch, eine Klage, ein Eilantrag oder eine Stellungnahme vor dem Sozialgericht praktisch tragfähig ist. Er soll Bürgern helfen, nichts Wichtiges zu vergessen.

## Wann aktivieren?

- Vor Absenden eines Widerspruchs.
- Vor Klageeinreichung.
- Vor einem Eilantrag.
- Vor Stellungnahme zu einem Gutachten.
- Vor mündlicher Verhandlung.
- Nach SG-Urteil vor Berufung oder Nichtzulassungsbeschwerde.

## Prüfmatrix

| Prüfungslinie | Kernfrage | Ampel |
|---|---|---|
| Frist | Ist Widerspruchs-, Klage- oder Berufungsfrist sicher? | Rot/Gelb/Grün |
| Bescheidkette | Liegen Ausgangsbescheid und Widerspruchsbescheid vor? | Rot/Gelb/Grün |
| Gericht | Ist das Sozialgericht zuständig? | Rot/Gelb/Grün |
| Klageart | Anfechtung, Verpflichtung, Leistung, Feststellung oder Untätigkeit? | Rot/Gelb/Grün |
| Eilbedarf | Muss § 86b SGG geprüft werden? | Rot/Gelb/Grün |
| Antrag | Sagt der Antrag genau, was die Behörde tun soll? | Rot/Gelb/Grün |
| Tatsachen | Sind Zeitraum, Personen, Leistungen und Bescheide klar? | Rot/Gelb/Grün |
| Belege | Sind die wichtigsten Nachweise beigefügt oder beantragt? | Rot/Gelb/Grün |
| Medizin | Gibt es aktuelle Befundberichte oder Gutachten? | Rot/Gelb/Grün |
| Kosten | § 183 SGG, § 193 SGG, § 109 SGG und PKH bedacht? | Rot/Gelb/Grün |

## Rote Flaggen

Empfehlen Sie Sozialverband, Anwalt, Beratungsstelle oder PKH-Prüfung besonders deutlich bei:

- Leistung aktuell gestoppt, Wohnung/Existenz/Gesundheit gefährdet;
- medizinische Gutachten widersprechen sich;
- mehrere Bescheide und Zeiträume sind vermischt;
- Frist läuft in weniger als sieben Tagen ab;
- Berufung, Nichtzulassungsbeschwerde oder BSG-Verfahren;
- § 109 SGG-Gutachten mit Kostenrisiko;
- Rückforderung oder Sanktion mit hohem Betrag;
- Nutzer kann den Antrag nicht in einem Satz erklären.

## Ablauf

### 1. Verfahrensstand bestimmen

| Dokument | Typischer nächster Schritt |
|---|---|
| Ausgangsbescheid | Widerspruch |
| Widerspruchsbescheid | Klage |
| Behörde schweigt | Untätigkeitsklage |
| Leistung fehlt sofort | Eilantrag |
| Gutachten liegt vor | Stellungnahme/Einwendungen |
| SG-Urteil | Berufung/Zulassung prüfen |

### 2. Antrag schärfen

Der Antrag soll so einfach wie möglich sagen:

```text
Ich beantrage, den Bescheid vom [Datum] in Gestalt des Widerspruchsbescheids vom [Datum] aufzuheben und die Beklagte zu verpflichten, mir [Leistung] ab [Datum] zu gewähren.
```

Für Eilfälle:

```text
Ich beantrage im Wege der einstweiligen Anordnung, die Antragsgegnerin vorläufig zu verpflichten, mir [Leistung] ab sofort bis zur Entscheidung in der Hauptsache zu gewähren.
```

### 3. Belege prüfen

| Thema | Belege |
|---|---|
| Bürgergeld | Bescheid, Kontoauszüge, Mietvertrag, Nebenkosten, Schriftverkehr |
| Krankenkasse | ärztliche Verordnung, Befundbericht, Ablehnung, MD-Stellungnahme |
| Pflegegrad | Pflegegutachten, Pflegetagebuch, Arztberichte, Hilfebedarf nach Modulen |
| EM-Rente | Befundberichte, Reha-Entlassungsbericht, Tätigkeitsbeschreibung |
| GdB | Diagnosen, Funktionsbeeinträchtigungen, Befunde, Alltagsschilderung |

## Ausgabeformat

**Sanity-Check**
| Feld | Ampel | Befund | Reparatur |
|---|---|---|---|

**Vor Absenden erledigen**
1. [kritischer Punkt]

**So kann es raus, wenn**
1. [Bedingung]

**Nächste Skills**
- `widerspruchsfrist-84-sgg`
- `klagearten-uebersicht-sgg`
- `eilantrag-86b-sgg-grundlagen`
- `zulassungsgrenzen-check-sozialgericht`

## Qualitätsregeln

- Fristen mit Datum und Ausgangspunkt nennen.
- Amtsermittlung nicht überschätzen: Belege bleiben wichtig.
- Bei Eilrechtsschutz immer Anordnungsanspruch und Anordnungsgrund trennen.
- Keine ärztlichen Diagnosen erfinden; medizinische Angaben nur aus Unterlagen übernehmen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
