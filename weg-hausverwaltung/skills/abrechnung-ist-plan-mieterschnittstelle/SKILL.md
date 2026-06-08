---
name: abrechnung-ist-plan-mieterschnittstelle
description: "Jahresabrechnung, Wirtschaftsplan und Mieterschnittstelle: trennt § 28 WEG-Nachschüsse/Vorschussanpassung von mietrechtlicher Betriebskostenabrechnung, prüft Ist-/Plan-Abweichungen, Umlagefähigkeit, Gewerbeanteile, Belege, Heizkosten/CO2 und Eigentümerdatenpakete."
---

# Abrechnung, Ist/Plan und Mieterschnittstelle

## Fachlicher Anker

- **Normen:** §§ 535, §§ 18, § 16 Abs. 2.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Abrechnung, Ist/Plan und Mieterschnittstelle
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.

Anwendungsfall: jahresabrechnung, Wirtschaftsplan, Betriebskostenabrechnung für Mieter und Eigentümerabrechnung zusammenstoßen.

## Kerntrennung

- **WEG-Jahresabrechnung:** Verhältnis Gemeinschaft/Eigentümer, Nachschüsse und Anpassung der Vorschüsse.
- **Wirtschaftsplan:** Zukunftsbudget und Vorschüsse.
- **Betriebskostenabrechnung:** Verhältnis Vermieter/Mieter, nur umlagefähige Kosten nach Mietvertrag und BetrKV.
- **Gewerbe:** Restaurant/Laden kann Kosten verursachen, die nicht ohne Weiteres gleichmäßig verteilt werden dürfen.

## Rechtsanker

- § 28 Abs. 1 WEG: Wirtschaftsplan und Vorschüsse.
- § 28 Abs. 2 WEG: Nachschüsse und Anpassung der beschlossenen Vorschüsse nach Ablauf des Kalenderjahres.
- § 556 BGB: mietrechtliche Abrechnung, Frist und Einwendungen.
- BetrKV, HeizkostenV, CO2KostAufG für die Übersetzung in die Mieterabrechnung.
- BGH, Urteil vom 19.07.2024 - V ZR 102/23: Beschlüsse zu Jahresabrechnung/Wirtschaftsplan sind nach neuem Recht auf Vorschüsse, Nachschüsse und Vorschussanpassungen auszulegen.
- BGH, Urteil vom 20.09.2024 - V ZR 195/23: Fehler der Jahresabrechnung sind für die Ungültigkeit relevant, wenn sie die Abrechnungsspitze/Zahlungspflicht betreffen.

## Prüfraster

| Position | Ist 2025 | Plan 2026 | Umlagefähig Mieter? | Schlüssel | Risiko |
| --- | --- | --- | --- | --- | --- |
| Heizung | [...] | [...] | [...] | [...] | [...] |
| Wasser | [...] | [...] | [...] | [...] | [...] |
| Hausmeister | [...] | [...] | [...] | [...] | [...] |
| Versicherung | [...] | [...] | [...] | [...] | [...] |
| Instandhaltung | [...] | [...] | regelmäßig nein | [...] | [...] |
| Gewerbe-Sonderkosten | [...] | [...] | prüfen | [...] | [...] |

## Mieterschnittstelle

Vermietende Eigentümer brauchen oft zwei Auswertungen:

1. **WEG-Prüfung:** Ist die Abrechnung gegenüber dem Eigentümer korrekt?
2. **Mieterprüfung:** Welche Positionen dürfen in die Betriebskostenabrechnung?
3. **Fristprüfung:** Abrechnungsfrist und Einwendungsfrist im Mietverhältnis.
4. **Belegpaket:** Rechnungen, Verträge, Verteilerschlüssel, Heizkostenabrechnung.

## Datenpaket für vermietende Eigentümer

Erzeuge auf Wunsch ein exportfähiges Paket:

1. umlagefähige Kosten nach BetrKV,
2. nicht umlagefähige Kosten mit Begründung,
3. HeizkostenV-Anlage,
4. CO2KostAufG-Anlage,
5. Vorauszahlungs-/Hausgeld-Soll-Ist-Abgleich,
6. Schlüsseldatei: MEA, Wohnfläche, Verbrauch, Gewerbe-Vorwegabzug,
7. Belegliste mit Zahlungsbelegen.

## Red Flags

- Erhaltungskosten in Betriebskostenabrechnung.
- Gewerbekosten auf alle Wohnungen verteilt ohne Schlüsselprüfung.
- CO2-Kosten falsch oder gar nicht verteilt.
- Ist-Kosten weichen stark vom Plan ab, ohne Erläuterung.
- Vermögensbericht fehlt oder ist mit Abrechnung vermischt.
- "Genehmigung der Jahresabrechnung" als Beschlusstext ohne Klarstellung auf Nachschüsse/Vorschussanpassung.
- vermietender Eigentümer erhält WEG-Abrechnung so spät, dass § 556 Abs. 3 BGB im Mietverhältnis brennt.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 20 WEG
- § 16 WEG
- § 28 WEG
- § 24 WEG
- § 21 WEG
- § 45 WEG
- § 23 WEG
- § 25 WEG
- § 26 WEG
- § 27 WEG
- § 25 TDDDG
- § 5 DDG

### Leitentscheidungen

- BGH V ZR 17/24
- BGH V ZR 34/24
- BGH V ZR 33/23
- BGH V ZR 102/23
- BGH V ZR 1/24

