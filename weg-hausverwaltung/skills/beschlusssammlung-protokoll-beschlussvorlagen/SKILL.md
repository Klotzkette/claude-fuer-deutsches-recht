---
name: beschlusssammlung-protokoll-beschlussvorlagen
description: "Beschlusssammlung Protokoll Beschlussvorlagen im Plugin Weg Hausverwaltung: prüft konkret Erstellt und prüft Protokoll, Beschlussverkündung, Beschlusssammlung (§ 24 Abs, Erstellt WEG-Beschlussvorlagen mit Beschlusskompetenz. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Beschlusssammlung Protokoll Beschlussvorlagen

## Arbeitsbereich

**Beschlusssammlung Protokoll Beschlussvorlagen** ordnet den Fall über die tragenden Prüfungslinien: Erstellt und prüft Protokoll, Beschlussverkündung, Beschlusssammlung (§ 24 Abs. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `beschlusssammlung-protokoll` | Erstellt und prüft Protokoll, Beschlussverkündung, Beschlusssammlung (§ 24 Abs. 7 WEG), Anlagenverweise, Abstimmungsergebnis, Nachversand und Dokumentationsstand (Stand 05/2026). Sorgt dafür, dass Auslegungsfragen späterer Beschlussklagen (z. B. BGH V ZR 102/23 zu Abrechnungsbeschlüssen) nicht entstehen. |
| `beschlussvorlagen-erstellen` | Erstellt WEG-Beschlussvorlagen mit Beschlusskompetenz, Kostenfolge, Ausführungsdetails, Alternativen, Begründung, Anlagenverweis und Anfechtungsrisiko (Stand 05/2026). Liefert Mustertexte für Abrechnungsspitzen, Sonderumlage, Schlüsseländerung mit sachlichem Grund, bauliche Veränderungen und Verwaltervergabe. |
| `betriebskosten-nebenkostenabrechnung` | WEG- und Hausverwaltungs-Schnittstelle Betriebskosten: erstellt und kontrolliert mietrechtliche Betriebskostenabrechnungen aus WEG-Jahresabrechnung, Wirtschaftsplan, Heizkostenabrechnung und Belegen; mit BetrKV, HeizkostenV, CO2KostAufG, § 556 BGB, Abrechnungsspitze und Datenpaket für vermietende Eigentümer. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WEG §§ 9a, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 44, 45, 46, 47, BGB §§ 535 ff., HOAI, BetrKV — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `beschlusssammlung-protokoll`

**Fokus:** Erstellt und prüft Protokoll, Beschlussverkündung, Beschlusssammlung (§ 24 Abs. 7 WEG), Anlagenverweise, Abstimmungsergebnis, Nachversand und Dokumentationsstand (Stand 05/2026). Sorgt dafür, dass Auslegungsfragen späterer Beschlussklagen (z. B. BGH V ZR 102/23 zu Abrechnungsbeschlüssen) nicht entstehen.

### Beschlusssammlung und Protokoll

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Beschlusssammlung und Protokoll` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Beschlusssammlung und Protokoll
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.

Stand: 05/2026.

## Ziel

Die Nachbereitung einer Eigentümerversammlung so dokumentieren, dass später klar ist, was beschlossen wurde, mit welcher Mehrheit, zu welchen Kosten und auf welcher Grundlage.

## Protokollfelder

- **Versammlungsdaten**: Datum, Ort, Format (physisch/virtuell/hybrid), Beginn/Ende.
- **Teilnehmende**: Anwesende, Vertretene, Vollmachten, Versammlungsleitung, Protokollführung.
- **Stimmrechte und MEA**: Liste je Einheit, ggf. Stimmverbote (§ 25 Abs. 4 WEG) dokumentiert.
- **Tagesordnungspunkt und Beschlusswortlaut** (vollständig, nicht zusammengefasst).
- **Abstimmungsergebnis** mit Ja / Nein / Enthaltung und ggf. MEA, sofern relevant.
- **Feststellung und Verkündung** durch Versammlungsleitung.
- **Anlagen und Angebote** mit Quelle und Stand.
- **Umsetzungsauftrag**: Wer macht was bis wann, mit welcher Vollmacht, welchem Budget, welcher Berichterstattung?
- **Hinweise auf Erkundigungsobliegenheit**: Eigentümer, die anfechten wollen, sollten daran erinnert werden, dass nach BGH, Urteil vom 25.10.2024, V ZR 17/24 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=25.10.2024&Aktenzeichen=V+ZR+17/24) bei Zustellungsverzug innerhalb eines Jahres beim Gericht der Sachstand zu erfragen ist.

## Auslegungssicherheit

- TOP zu Jahresabrechnung **immer** als "Abrechnungsspitzen" formulieren — vermeidet die nachträgliche Auslegungskonstruktion aus BGH, Urteil vom 19.07.2024, V ZR 102/23 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.07.2024&Aktenzeichen=V+ZR+102/23).
- Bei Schlüsseländerung den sachlichen Grund **schriftlich** ins Protokoll aufnehmen (Bezug zu BGH, Urteile vom 14.02.2025, V ZR 236/23 und V ZR 128/23).
- Bei Gestattungsbeschluss zur baulichen Veränderung Auflagen aus dem Wortlaut und nicht nur aus der Anlage erkennbar machen.

## Beschlusssammlung (§ 24 Abs. 7 WEG)

Tabellarisch mit:

| lfd. Nr. | Datum | TOP | Beschlusswortlaut | Ergebnis (Ja/Nein/Enth.) | Status (gültig, angefochten, aufgehoben) | Anfechtungshinweis | Umsetzung | Ablageort |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

- **Unverzüglich** nach Verkündung eintragen.
- Bei späterer Aufhebung / Anfechtungsurteil: Eintragung ergänzen, ursprünglichen Eintrag stehen lassen (Historie).

## Mustertext "Nachversand"

> Sehr geehrte Eigentümer,
> anliegend übersende ich Ihnen das Protokoll der Eigentümerversammlung vom [Datum] (Anlage 1) sowie die Beschlüsse Nr. [...] bis [...].
> Die Beschlüsse sind in die Beschlusssammlung gem. § 24 Abs. 7 WEG eingetragen.
> **Hinweis Anfechtungsfristen**: Eine Beschlussanfechtungsklage muss innerhalb eines Monats ab Beschlussfassung erhoben und innerhalb von zwei Monaten begründet werden (§ 45 WEG). Bei Zustellungsverzögerungen empfiehlt sich, innerhalb eines Jahres beim Gericht den Sachstand zu erfragen (BGH, V ZR 17/24).
> Für Rückfragen stehe ich Ihnen zur Verfügung.

## Output

- Protokollentwurf
- Beschlusssammlungseintrag (tabellarisch)
- Nachversand-Mail
- Umsetzungs-Tracker (Aufgabe, Zuständig, Frist, Status)

## Cross-Refs

- Anfechtungsrisiko → `beschlussanfechtung-risiko`
- Vorbereitung Versammlung → `eigentuemerversammlung-vorbereiten`
- Beschlussformulierung → `beschlussvorlagen-erstellen`

## Quellenpflicht

`rechtsstand-mai-2026-faktenbank` laden. § 24 Abs. 7 WEG: https://www.gesetze-im-internet.de/woeigg/__24.html .

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `beschlussvorlagen-erstellen`

**Fokus:** Erstellt WEG-Beschlussvorlagen mit Beschlusskompetenz, Kostenfolge, Ausführungsdetails, Alternativen, Begründung, Anlagenverweis und Anfechtungsrisiko (Stand 05/2026). Liefert Mustertexte für Abrechnungsspitzen, Sonderumlage, Schlüsseländerung mit sachlichem Grund, bauliche Veränderungen und Verwaltervergabe.

### Beschlussvorlagen Erstellen

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Beschlussvorlagen Erstellen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Beschlussvorlagen Erstellen
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.

Stand: 05/2026.

## Ziel

Aus einem Verwaltungsthema wird ein klarer Beschlussantrag, der nicht zu viel und nicht zu wenig regelt.

## Aufbau

1. **Beschlussgegenstand**: Was wird entschieden? (Ein Satz.)
2. **Rechts- und Kompetenzanker**: WEG-Norm, Gemeinschaftsordnung, Vorbeschlüsse, BGH-Anker.
3. **Ausführung**: Wer beauftragt wen, bis wann, mit welchem Budget, mit welcher Vollmacht?
4. **Kostenfolge**: Schlüssel, Sonderumlage, Rücklage, Wirtschaftsplan, Fälligkeit. Bei Schlüsseländerung: sachlicher Grund (siehe BGH V ZR 236/23, V ZR 128/23 vom 14.02.2025).
5. **Kontrolle**: Beirat, Vergleichsangebote, Abnahme, Gewährleistung, Berichtspflicht.
6. **Alternativen**: Nullvariante, kleinere Lösung, Höchstpreisdeckel, Vertagung mit Frist.

## Stilregeln

- Ein Beschluss, ein Gedanke.
- Keine versteckten Nebenentscheidungen ("im Übrigen" - "soweit erforderlich").
- Kosten, Schlüssel und Vollmacht ausdrücklich.
- Anlagen präzise benennen ("Angebot Fa. X vom [Datum], Anlage 4").
- Bei baulichen Veränderungen: Trennung von Gestattung (§ 20 WEG) und Kostentragung (§ 21 WEG) im Wortlaut.

## Mustertexte

### Abrechnungsspitzen (§ 28 Abs. 2 WEG)

> Die Wohnungseigentümer beschließen auf der Grundlage der Jahresabrechnung [Jahr] (Anlage 1):
> 1. Die sich aus der Jahresabrechnung ergebenden Nachschüsse / Anpassungen der Vorschüsse gemäß den Einzelabrechnungen (Anlage 2).
> 2. Fälligkeit der Nachschüsse: [Datum].
> 3. Guthaben werden bis [Datum] mit nächsten Hausgeldzahlungen verrechnet.
> 4. Der Vermögensbericht zum [Stichtag] (Anlage 3) wird zur Kenntnis genommen.

### Wirtschaftsplan (§ 28 Abs. 1 WEG)

> Die Wohnungseigentümer beschließen den Wirtschaftsplan [Jahr] (Anlage 1) sowie die hieraus resultierenden Vorschüsse je Einheit gemäß Anlage 2. Fälligkeit monatlich zum [Tag], beginnend mit [Monat/Jahr].

### Sonderumlage

> Die Wohnungseigentümer beschließen eine Sonderumlage in Höhe von [Betrag] EUR zur Finanzierung von [Zweck]. Verteilung nach allgemeinem Kostenschlüssel (MEA / Einheiten) gemäß Anlage [X]. Fälligkeit [Datum / X Werktage nach Zugang der Einzelabrechnung]. Buchung auf einem zweckgebundenen Konto der GdWE.

### Schlüsseländerung mit sachlichem Grund (§ 16 Abs. 2 Satz 2 WEG)

> Die Wohnungseigentümer beschließen, den Kostenverteilungsschlüssel für [Kostenart, z. B. Wärmeerzeugung / Erhaltungsrücklage] von [alt] auf [neu] zu ändern.
> **Sachlicher Grund**: [konkrete Begründung, z. B. der bisherige Schlüssel privilegiert die Gewerbeeinheiten ohne sachlichen Grund; die geänderte Verteilung entspricht dem tatsächlichen Nutzen / dem aktuellen Verbrauchsverhältnis; vgl. BGH, Urteile vom 14.02.2025, V ZR 236/23 und V ZR 128/23].
> Die Änderung gilt für Abrechnungen ab dem [Datum].

### Bauliche Veränderung (Gestattung + Kostenfolge getrennt)

> 1. (Gestattung): Den Eigentümern der Einheit Nr. [...] wird gestattet, [Maßnahme] gemäß Anlage [X] mit den dort beschriebenen Auflagen (Optik, Versicherung, Wartung, Rückbau) zu errichten.
> 2. (Kostenfolge): Die Kosten der baulichen Veränderung sowie Folgekosten (Wartung, Versicherung, Rückbau) trägt der Antragsteller allein (§ 21 Abs. 1 WEG).

### Verwaltervergabe / Bestellung

> Die Wohnungseigentümer bestellen [Firma] zum Verwalter der WEG für die Dauer von [Laufzeit, max. 5 Jahre] beginnend zum [Datum]. Der Verwaltervertrag gemäß Anlage [X] wird beschlossen; die Verwaltung wird ermächtigt, ihn nach Maßgabe der Anlage zu unterzeichnen.

### Schadensbearbeitung über GdWE (nach BGH V ZR 34/24)

> Die Wohnungseigentümer beschließen, den Anspruch auf Ersatz des Schadens [Sachverhalt] gegenüber der GdWE geltend zu machen; die Verwaltung wird beauftragt, etwaige Regressansprüche der GdWE gegenüber dem (vormaligen) Verwalter zu prüfen und ggf. geltend zu machen.

## Output

- Beschlussvorlage kurz (für TOP-Block)
- Beschlussvorlage ausführlich (mit Begründung)
- Begründungstext für Einladung
- Risikoampel (Kompetenz, Bestimmtheit, Kostenfolge, Vorbefassung)
- Anlagenliste

## Cross-Refs

- Vorbefassung / Anfechtung → `beschlussanfechtung-risiko`
- Einladung / Tagesordnung → `einladung-tagesordnung-fristen`
- Bauliche Veränderungen → `bauliche-veraenderungen-20-weg`, `steckersolar-wallbox-barrierefreiheit`
- Liquidität / Sonderumlage → `hausgeld-sonderumlage-liquiditaet`

## Quellenpflicht

`rechtsstand-mai-2026-faktenbank` laden. Rechtsprechungsaussagen nur mit offen prüfbarer Quelle.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `betriebskosten-nebenkostenabrechnung`

**Fokus:** WEG- und Hausverwaltungs-Schnittstelle Betriebskosten: erstellt und kontrolliert mietrechtliche Betriebskostenabrechnungen aus WEG-Jahresabrechnung, Wirtschaftsplan, Heizkostenabrechnung und Belegen; mit BetrKV, HeizkostenV, CO2KostAufG, § 556 BGB, Abrechnungsspitze und Datenpaket für vermietende Eigentümer.

### Betriebskosten und Nebenkosten in der WEG-Verwaltung

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Betriebskosten und Nebenkosten in der WEG-Verwaltung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Betriebskosten und Nebenkosten in der WEG-Verwaltung
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.

Stand: 05/2026.

## Ziel

Die Hausverwaltung soll zwei Welten auseinanderhalten:

- **WEG-Rechnung**: GdWE, Eigentümer, Nachschüsse und Vorschussanpassung nach § 28 Abs. 2 WEG.
- **Mietrechtliche Betriebskostenabrechnung**: Vermieter, Mieter, Umlagevereinbarung, BetrKV, HeizkostenV, CO2KostAufG, § 556 BGB.

Eine WEG-Einzelabrechnung ist kein fertiger Mieternebenkostenbescheid. Sie ist Rohmaterial.

## Einstieg

1. Wer fragt: WEG-Verwalter, vermietender Eigentümer, Mieter, Anwalt?
2. Geht es um Erstellung, Prüfung, Datenanforderung oder Streit?
3. Welche Unterlagen liegen vor: Jahresabrechnung, Einzelabrechnung, Wirtschaftsplan, Heizkosten, CO2, Rechnungen, Zahlungsbelege?
4. Wohnraum, Gewerbeeinheit oder gemischte Nutzung?
5. Soll ein Mieteranschreiben, Eigentümerdatenpaket, Belegeinsichtsprotokoll oder Beschluss-/Anfechtungsvermerk entstehen?

## Prüfung

- **Umlagefähigkeit** nach Mietvertrag (Klausel auf BetrKV verweisend) und BetrKV (https://www.gesetze-im-internet.de/betrkv/).
- **Abrechnungszeitraum**: in der Regel Kalenderjahr; muss im Mietvertrag oder konsequent praktiziert sein.
- **Zugangsfrist**: Vermieter muss innerhalb von **12 Monaten** ab Ende des Abrechnungszeitraums abrechnen (§ 556 Abs. 3 BGB — https://www.gesetze-im-internet.de/bgb/__556.html). Nach Ablauf nur noch zugunsten des Mieters Korrekturen möglich.
- **Verteilerschlüssel** nach Mietvertrag, Wohnfläche, Verbrauch oder Einheiten; bei Heizung/Warmwasser zwingend nach HeizkostenV: verbrauchsabhängiger Anteil mindestens 50 % und höchstens 70 %, der restliche Anteil (30 % bis 50 %) nach Wohnfläche oder umbautem Raum (§§ 7, 8 HeizkostenV — https://www.gesetze-im-internet.de/heizkostenv/). Der häufige Schlüssel 70/30 (70 % Verbrauch, 30 % Fläche) ist eine zulässige Ausgestaltung innerhalb dieser Bandbreite, nicht die einzige.
- **HeizkostenV**: Erfassung, Verteilung, Ablesung, Zwischenablesung bei Mieterwechsel.
- **Nicht umlagefähig**: Verwaltungskosten, Instandsetzung/Erhaltung (vs. Wartung), Bankgebühren ohne Vertragsgrundlage, Reparaturen, Erhaltungsrücklage.
- **Belegeinsicht** nach Aufforderung; Vermieter muss Einsicht ermöglichen, ggf. gegen Kostenerstattung Kopien.
- **Einwendungen** des Mieters: innerhalb 12 Monaten ab Zugang der Abrechnung (§ 556 Abs. 3 Satz 5 BGB).

## WEG-spezifische Übersetzung

| WEG-Position | Mietrechtliche Behandlung | Warnung |
| --- | --- | --- |
| Verwalterhonorar | nicht umlagefähig | aus Mieterabrechnung herausnehmen |
| Erhaltungsrücklage | nicht umlagefähig | keine Betriebskosten |
| Reparatur/Instandsetzung | nicht umlagefähig | Wartung/Reparatur trennen |
| Hausmeister | nur laufende, umlagefähige Tätigkeiten | Tätigkeitsliste verlangen |
| Versicherung | umlagefähig nur bei Grundstücksbezug | Police prüfen |
| Gewerbe-Sonderkosten | Vorwegabzug möglich/nötig | Restaurant/Praxis/Tiefgarage separat prüfen |
| Heizkosten | HeizkostenV gesondert | nicht in allgemeine Fläche ziehen |
| CO2-Kosten | CO2KostAufG | Vermieteranteil nicht umlagen |

## Abrechnungsspitze und Beschluss

Seit der WEG-Reform beschließen Eigentümer nicht mehr die Jahresabrechnung "als solche", sondern die Einforderung von Nachschüssen oder Anpassung der Vorschüsse. Fehler im Zahlenwerk sind für eine Anfechtung besonders relevant, wenn sie sich auf die Abrechnungsspitze und damit die Zahlungspflicht auswirken. Für die Mieterseite bleibt zusätzlich die mietrechtliche Umrechnung nötig.

## CO2KostAufG (seit 01.01.2023)

- Verteilung der CO₂-Kosten zwischen Vermieter und Mieter nach Zehn-Stufen-Modell (kg CO₂/m²·a).
- Hoch-Emissionsgebäude: Vermieter trägt 95 %, Mieter 5 %. EH-55-Neubau: Mieter 100 %.
- Nichtwohngebäude: derzeit grundsätzlich hälftige Aufteilung, kein verbindliches Stufenmodell "ab 2025" behaupten.
- WEG-Abrechnung sollte die für die Stufenermittlung erforderlichen Daten (Brennstoffmenge, Emissionsfaktor, Energieausweis-Werte) liefern, damit der vermietende Eigentümer die Aufteilung mietvertraglich umsetzen kann.
- Quelle: https://www.gesetze-im-internet.de/co2kostaufg/

## Mietpreisbremse — Schnittstelle

- Mietpreisbremse §§ 556d ff. BGB ist bis **31.12.2029** verlängert (Gesetz vom 17.07.2025, BGBl. 2025 I Nr. 163: https://www.recht.bund.de/bgbl/1/2025/163/VO.html, Inkrafttreten 23.07.2025); gilt in Gebieten, die durch Landesrechtsverordnung als angespannte Wohnungsmärkte ausgewiesen sind.
- Auswirkung auf Betriebskostenabrechnung: keine direkte; aber bei Nettokaltmiete-Korrekturen Hinweis auf erlaubte Höchstmiete prüfen.

## Mustertext Einwendung Mieter

> Sehr geehrte Damen und Herren,
> hinsichtlich der Betriebskostenabrechnung [Jahr] vom [Datum] erhebe ich folgende Einwendungen:
> 1. Position [...]: nicht umlagefähig nach BetrKV (Begründung: [...]).
> 2. Position [...]: Schlüssel weicht von mietvertraglicher Vereinbarung ab (vereinbart [...] statt verwendet [...]).
> 3. Position [...]: rechnerische Unstimmigkeit (Summe [...] passt nicht zu Einzelposten [...]).
> Ich bitte um Belegeinsicht und Korrektur innerhalb von [Frist].

## Prüf-Tabelle (Schema)

| Position | Umlagefähig? (BetrKV) | Schlüssel ok? | Plausibilität / Beleg | Korrekturbedarf |
| --- | --- | --- | --- | --- |
| Heizung/Warmwasser | ja (BetrKV Nr. 4) | HeizkostenV beachtet? | Verbrauchsdaten, Brennstoff | ggf. CO₂-Aufteilung |
| Wasser/Abwasser | ja | Verbrauch/Einheiten | Zähler/Rechnung | |
| Müll | ja | Einheiten/Wohnfläche | kommunale Gebühren | |
| Hausmeister | ja, soweit nicht Reparatur | Vertrag/Stundenliste | Stundennachweise | Aussonderung von Reparaturen |
| Verwalterkosten WEG | nein (Verwaltungskosten) | — | — | herausnehmen |

## Output

- Prüftabelle Kostenpositionen
- Rückfragen an Verwaltung (WEG-seitig)
- Mieter-/Vermieter-Antwortentwurf
- Korrekturvorschlag mit beziffertem Erstattungs-/Nachforderungsbetrag
- Hinweis auf CO2KostAufG-Aufteilung
- Datenpaket für vermietende Eigentümer: umlagefähige Positionen, nicht umlagefähige Positionen, Heizkosten/CO2, Belegliste, Schlüssel

## Cross-Refs

- WEG-Abrechnungsseite → `wirtschaftsplan-jahresabrechnung-28-weg`
- Vermietender Eigentümer / Datenfluss → `verwalterpflichten-26-27-weg`
- Eskalation → `eskalation-anwalt-amtsgericht`
- Mietrecht-Plugin als Schnittstelle

## Quellenpflicht

`rechtsstand-mai-2026-faktenbank` laden. BetrKV: https://www.gesetze-im-internet.de/betrkv/ ; HeizkostenV: https://www.gesetze-im-internet.de/heizkostenv/ ; § 556 BGB: https://www.gesetze-im-internet.de/bgb/__556.html ; CO2KostAufG: https://www.gesetze-im-internet.de/co2kostaufg/ .

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
