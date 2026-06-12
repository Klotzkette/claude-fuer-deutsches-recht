---
name: dsfa-risikoanalyse
description: "Risikoanalyse im Rahmen der DSFA: Eintrittswahrscheinlichkeit mal Schadenschwere für Bedrohungsszenarien systematisch ermitteln. Output: Risikomatrix mit Begruendung Ampelfarbe und Begruendung der Stufung."
---

# Risikoanalyse Eintrittswahrscheinlichkeit mal Schadenschwere

## Wann dieses Modul hilft

- In jeder vollstaendigen DSFA
- Bei Aktualisierung einer DSFA nach wesentlicher Änderung
- Bei DSB-Stellungnahme, wenn die Risikobewertung pauschal blieb
- Bei Aufsichtsanstoss, wenn die Risikomethodik gegruendet werden muss

## Rechtlicher Rahmen

- Art. 35 Abs. 7 lit. c DSGVO: Bewertung der Risiken für die Rechte und Freiheiten der Betroffenen.
- EDSA-Leitlinien WP 248 rev.01 mit Risiko-Skalen.
- ENISA-Leitfaden zur DSFA — Methodik für Eintrittswahrscheinlichkeit und Schadenschwere.
- Erwaegungsgrund 75 DSGVO: Beispiele für materielle und immaterielle Schaeden (Diskriminierung, Identitaetsdiebstahl, finanzieller Verlust, Rufschaedigung, Verlust der Vertraulichkeit besonders geschuetzter Daten).
- Erwaegungsgrund 76 DSGVO: Risiko ist anhand einer objektiven Bewertung zu beurteilen.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Datenfluss, Datenarten, Empfaenger, Aufbewahrung, Technologie — als Grundlage für die Bedrohungsanalyse.
2. **Verhältnismäßigkeitspruefung.** Welche Schutzziele sind beruehrt (Vertraulichkeit, Integritaet, Verfuegbarkeit, Transparenz, Intervenierbarkeit, Nicht-Verkettung, Datenminimierung)?
3. **Risikoanalyse.** Pro Schutzziel Bedrohungsszenarien definieren:
 - Vertraulichkeit: unbefugter Zugriff, Datenleck, Insider-Zugriff
 - Integritaet: unbemerkte Änderung, Manipulation
 - Verfuegbarkeit: Ausfall, Loeschung, Ransomware
 - Transparenz: verdeckte Verarbeitung, fehlende Information
 - Intervenierbarkeit: Loeschungs- oder Berichtigungssperre
 - Nicht-Verkettung: ungewollte Zusammenfuehrung
 - Datenminimierung: über Zweck hinausreichende Speicherung
 Pro Szenario: Eintrittswahrscheinlichkeit (gering/mittel/hoch) und Schadenschwere für Betroffene (gering/mittel/hoch). Verknuepfung zur Risikostufe nach Matrix.
4. **Maßnahmen.** Wirkung der geplanten Maßnahmen auf Wahrscheinlichkeit und Schwere; Prüfung ob die Risikostufe sinkt.
5. **Restrisiko.** Risikostufe nach Maßnahmen, dokumentiert pro Szenario. Wenn hoch verbleibend, Vorab-Konsultation nach Art. 36.
6. **Konsultation / Genehmigung.** DSB-Stellungnahme; Risikomatrix in die DSFA als zentrales Steuerungsdokument einbetten.

## Bewertungsmatrix (3x3)

```
 Schadenschwere
 gering mittel hoch
Wahrscheinlichkeit
 hoch GELB ORANGE ROT
 mittel GRUEN GELB ORANGE
 gering GRUEN GRUEN GELB
```

- GRUEN — Risiko niedrig, dokumentieren
- GELB — Risiko mittel, Maßnahmen prüfen
- ORANGE — Risiko hoch, Maßnahmen verbindlich, ggf. Vorab-Konsultation
- ROT — Risiko sehr hoch, ohne Maßnahmen-Anpassung keine Freigabe

## Mustertext / Template

```
RISIKOMATRIX DSFA [DATUM]

Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME]
Methode: 3x3 Eintrittswahrscheinlichkeit x Schadenschwere

Szenario | W | S | Risiko vor | Massnahme | W' | S' | Risiko nach
1 Unbefugter Zugriff | h | h | ROT | [...] | g | h | GELB
2 Unbemerkte Datenmanipulation | m | h | ORANGE | [...] | g | m | GRUEN
3 Datenverlust durch Ausfall | m | m | GELB | [...] | g | m | GRUEN
4 Verdeckte Profilbildung | h | h | ROT | [...] | m | h | ORANGE
5 Loeschungssperre | g | m | GRUEN | [...] | g | m | GRUEN
6 Ungewollte Zusammenfuehrung | m | h | ORANGE | [...] | g | m | GRUEN
7 Ueberspeicherung | h | g | GELB | [...] | g | g | GRUEN

Begruendung Wahrscheinlichkeit: [Bedrohungsmodell, Erfahrungswerte, Statistik]
Begruendung Schadenschwere: [Erwaegungsgrund 75 DSGVO, Schutzbeduerftigkeit]

Gesamtrisiko vor Massnahmen: [HOCH]
Gesamtrisiko nach Massnahmen: [MITTEL]

Restrisiko hoch verbleibend: ja / nein
Bei ja: Vorab-Konsultation Art. 36 DSGVO erforderlich.

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________
```

## Typische Fehler

- Wahrscheinlichkeit ohne Bedrohungsmodell geschaetzt — Bauchwerte sind nicht aufsichtstauglich.
- Schadenschwere nur aus Sicht der Organisation bewertet — Maßstab ist der Betroffene (Erwaegungsgrund 75).
- Maßnahmenwirkung nicht beziffert — die Spalte nach Maßnahmen bleibt leer.
- Restrisiko hoch wird hingenommen ohne Art. 36 zu konsultieren — eigenstaendige Pflichtverletzung.
- Risikomatrix wird nicht aktualisiert — DSFA als Einmaldokument.
- Schutzziele werden auf Vertraulichkeit reduziert — Transparenz und Intervenierbarkeit werden vergessen.

## Quellen Stand 06/2026

- Art. 35 Abs. 7 lit. c DSGVO
- Erwaegungsgrund 75, 76 DSGVO
- EDSA-Leitlinien WP 248 rev.01
- ENISA — DSFA-Leitfaden
- SDM V3.0 — Schutzziele
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle
