---
name: datenqualitaet-xai
description: "Qualitaetskontrolle und Quellenvalidierung im Corporate/M&A-Mandat: Partner oder Counsel prüft KI-generierte DD-Findings auf fehlerhafte Quellen, Luecken in der Belegkette und Black-Box-Schluesse. Normen: BRAO § 43a (Sorgfaltspflicht), EU-KI-VO (AI Act) Art. 13 Transparenz. Prüfraster: Belegkette — Arbeitskontext: Corporate-Kanzlei (M&A, Gesellschaftsrecht), Schwerpunkt datenqualitaet xai."
---

# Datenqualität und Qualitätskontrolle im M&A-Mandat

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Triage — kläre vor jeder Analyse

1. Welche Datenquellen liegen vor — Datenraum, öffentliches Register, Gutachten, Managementangaben, Presseberichte?
2. Ist der Datenstand verifiziert und aktuell — Datum der letzten Aktualisierung, Version, Vollständigkeitsbestätigung des Verkäufers?
3. Welches Risikoniveau hat das Ergebnis — geht es in Board Paper, SPA-Warranty-Katalog, DD-Bericht oder nur interne Orientierung?
4. Wer ist Human-in-the-loop (Senior Associate, Counsel, Partner) und bis wann ist Senior Review einzuholen?
5. Gibt es bereits bekannte Datenlücken oder Widersprüche zwischen Quellen (z.B. HR-Zahlen vs. HGB-Anhang)?

## Zentrale Grundlagen

- **§ 93 Abs. 1 S. 2 AktG / § 43 Abs. 1 GmbHG** — Business Judgment Rule: Entscheidung muss auf angemessener Information beruhen; fehlerhafte Datenbasis = kein Safe Harbour.
- **§ 311 AktG** — Abhängigkeitsbericht: Datenqualität entscheidend für Nachteilsfeststellung.
- **§ 22 WpHG / Art. 17 MAR** — Insiderinformation: fehlerhafte Quellenattribution kann Marktmissbrauchsrisiko auslösen.
- **§§ 242, 264 HGB** — Buchführungspflichten: Verlässlichkeit der Finanzdaten als Prüfungsgrundlage.
- **DSGVO Art. 5 Abs. 1 lit. d** — Datenrichtigkeit: personenbezogene Daten müssen sachlich richtig und aktuell sein.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfmatrix Datenqualitätskontrolle

| Dimension | Prüffrage | Ampel | Massnahme bei Rot |
|---|---|---|---|
| Quellenursprung | Stammt Datum aus Primärquelle (Register, Jahresabschluss) oder Sekundärquelle (Zusammenfassung, Managementvorlage)? | Grün/Gelb/Rot | Primärquelle einholen oder Vorbehalt dokumentieren |
| Aktualität | Ist Datenstand nicht älter als [6 Monate]? Stichtag bekannt? | Grün/Gelb/Rot | Verkäuferbestätigung anfordern; Bringschuld in SPA |
| Vollständigkeit | Gibt es erkennbare Lücken — fehlende Perioden, fehlende Gesellschaften, fehlende Tochtergesellschaften? | Grün/Gelb/Rot | Informationsanforderungsliste (Q&A) aufsetzen |
| Konsistenz | Stimmen Daten in unterschiedlichen Quellen überein — HR-Zahlen = HGB-Anhang = Managementpräsentation? | Grün/Gelb/Rot | Abweichungsanalyse; Eskalation an Owner |
| Verlässlichkeit der Schlussfolgerung | Ist Schlussfolgerung aus Datenlage logisch zwingend oder spekulativ? | Grün/Gelb/Rot | Vorbehalt einfügen; Human-in-the-loop |
| Human-in-the-loop | Ist Senior Review vor Verwendung in Board Paper / SPA / DD-Bericht eingeholt? | Grün/Rot | Review dokumentieren; Keine Weiterverwendung ohne Freigabe |

## Schritt-für-Schritt-Workflow

1. **Quellen inventarisieren:** Alle Quellen mit Bezeichnung, Version, Datum, Datenraum-ID und Vollständigkeitsgrad in Belegkette erfassen.
2. **Risikolevel bestimmen:** Geht Ergebnis in Entscheidungsvorlage (hohes Risiko), DD-Bericht (mittleres Risiko) oder internen Vermerk (niedriges Risiko)?
3. **Konsistenzcheck:** Zahlen aus mindestens zwei unabhängigen Quellen gegenprüfen; Abweichungen > [10 %] als Konflikt markieren.
4. **Lückenanalyse:** Fehlende Daten als TODO mit Owner und Frist erfassen; keine Lücken stillschweigend interpolieren.
5. **Schlussfolgerungsprotokoll:** Jede analytische Schlussfolgerung mit Begründung und Unsicherheitsgrad versehen.
6. **Human-in-the-loop-Gate:** Bei Risikoniveau Hoch: Senior Review vor Weiterverwendung; Freigabe dokumentieren.
7. **Qualitätsprotokoll finalisieren:** Ergebnis mit Ampelstatus, Belegkette, offenen Punkten und Freigabegrad übergeben.

## Output-Template Qualitätsprotokoll

**Adressat:** Deal-Team intern — Tonfall sachlich-analytisch
```
DATENQUALITÄTSPROTOKOLL
Mandat: [Mandatsname / Deal-Bezeichnung]
Ersteller: [Name, Funktion]
Datum: [Datum]
Version: [Nr.]
Freigabe durch: [Name, Funktion, Datum]

ANALYSIERTES ERGEBNIS
Gegenstand: [kurze Beschreibung des Ergebnisses / der Schlussfolgerung]
Verwendungszweck: [Board Paper / DD-Bericht / SPA-Annex / interner Vermerk]
Risikoniveau: [Hoch / Mittel / Niedrig]

BELEGKETTE
| Nr. | Quelle | Dok-Bezeichnung | Version/Datum | Datenraum-ID | Vollständigkeitsstatus |
|----|--------|-----------------|--------------|--------------|----------------------|
| 1 | [Quelle] | [Bezeichnung] | [V/Datum] | [ID] | [Vollständig/Lücke] |

KONSISTENZPRÜFUNG
| Datenpunkt | Quelle 1 | Quelle 2 | Abweichung | Bewertung |
|-----------|---------|---------|-----------|-----------|
| [Punkt] | [Wert] | [Wert] | [%/EUR] | [OK/Konflikt] |

BEKANNTE DATENLÜCKEN
| Nr. | Fehlende Information | Auswirkung auf Analyse | Owner | Frist | Eskalation |
|----|---------------------|----------------------|-------|-------|------------|
| 1 | [Lücke] | [Gering/Mittel/Hoch] | [Name] | [Datum] | [Stufe] |

SCHLUSSFOLGERUNG
[Ergebnis in 2-3 Sätzen; Grad der Sicherheit; Vorbehalte]

HUMAN-IN-THE-LOOP
Senior Review eingeholt: [Ja / Nein / Ausstehend]
Reviewer: [Name, Funktion]
Freigabedatum: [Datum]
Freigabegrad: [Vollständig / Unter Vorbehalt / Abgelehnt]

OFFENE PUNKTE (TODO)
| Nr. | Punkt | Owner | Frist | Eskalationsstufe |
|----|-------|-------|-------|-----------------|
| 1 | [Punkt] | [Name] | [Datum] | [Partner/Counsel/Associate] |
```

## Rote Schwellen

- Schlussfolgerung geht in Board Paper oder SPA ohne dokumentierte Belegkette → Stop; Qualitätsprotokoll erstellen.
- Bekannte Datenlücke wird verschwiegen statt als Vorbehalt dokumentiert → Haftungsrisiko für Anwalt und GF/Vorstand.
- Human-in-the-loop-Gate übersprungen bei Risikoniveau Hoch → Senior Review sofort nachholen.
- Widersprüche zwischen Quellen > [10 %] ohne Klärung → Weitergabe stoppen; Eskalation an Owner.
- Ergebnis aus nicht verifizierbarer Sekundärquelle als Primärfakt dargestellt → Korrektur erforderlich.

## Strategische Hinweise

| Situation | Empfehlung |
|---|---|
| Managementangaben ohne schriftliche Grundlage | Als unverified markieren; schriftliche Bestätigung/Garantie im SPA verlangen |
| Datenraum-Dokument ohne Versionsnummer | Zeitstempel und Datenraum-ID als Proxy nutzen; Verkäufer um Versionshistorie bitten |
| Widersprüchliche Finanzzahlen | Buchhalterischen Beleg (Jahresabschluss, Steuerklarung) als Anker verwenden; Management um Überleitung bitten |
| Ergebnis unter Zeitdruck ohne vollständige Daten | Vorbehalt dokumentieren; Eskalationsschwelle klar benennen; Entscheidungsträger informieren |

## Quellen und Vertiefung

- §§ 93 AktG, 43 GmbHG (BJR-Informationspflicht)
- §§ 242, 264 HGB (Buchführungsqualität als Datengrundlage)
- Art. 5 Abs. 1 lit. d DSGVO (Datenrichtigkeit)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Übergabe an andere Skills

- `corporate-kanzlei-kommandocenter` — Gesamtkoordination; Eskalation bei roter Schwelle
- `corporate-kanzlei-board-paper-business-judgment` — Board Paper setzt Qualitätsprotokoll voraus
- `corporate-kanzlei-due-diligence-reporting` — DD-Report nur mit verifizierten Quellen
- `corporate-kanzlei-disclosure-schedules` — Disclosure nur mit vollständiger Belegkette
