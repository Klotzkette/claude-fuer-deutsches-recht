---
name: dsfa-methodik-cnil-pia-vs-bsfd-bsi
description: "Vergleich der DSFA-Methoden: CNIL PIA Software (Frankreich) gegenueber dem BSI Standard-Datenschutzmodell (SDM) und dem BSFD-Ansatz. Output: Methodenwahl mit Begruendung, Anwendungshinweisen und Werkzeugauswahl."
---

# DSFA-Methodik CNIL PIA versus SDM/BSI

## Wann dieses Modul hilft

- Vor der Erstdurchfuehrung einer DSFA, wenn keine Hausmethodik vorgegeben ist
- Beim Aufbau eines Datenschutzmanagementsystems (DSMS)
- Wenn die Aufsichtsbehoerde eine methodische Begruendung verlangt
- Bei grenzueberschreitenden Verarbeitungen (Frankreich-Bezug erleichtert CNIL-PIA)

## Rechtlicher Rahmen

- Art. 35 Abs. 7 DSGVO Mindestinhalte der DSFA — methodenoffen.
- EDSA-Leitlinien WP 248 rev.01 verweisen auf etablierte Methoden, ohne eine vorzuschreiben.
- CNIL PIA Methodology (Privacy Impact Assessment): freie Software der franzoesischen Datenschutzbehoerde CNIL, modular, dreiteilig (Knowledge Base, Methodology, Templates).
- Standard-Datenschutzmodell (SDM) der Datenschutzkonferenz: Schutzziele Vertraulichkeit, Integritaet, Verfuegbarkeit, Transparenz, Intervenierbarkeit, Nicht-Verkettung, Datenminimierung; Referenz für Aufsichtsverfahren in Deutschland.
- BSI-Grundschutz mit Datenschutz-Baustein: technische Bausteine mit Bezug zu Schutzbedarfsfeststellung; nicht primaer DSFA-spezifisch, aber kompatibel.

## Methoden im Vergleich

| Merkmal | CNIL PIA | SDM (DSK) | BSI-Grundschutz |
|---|---|---|---|
| Rechtsrahmen | DSGVO (FR) | DSGVO (DE) | IT-Sicherheit primaer |
| Werkzeug | Open-Source-Software | Methodenpapier | Fachüberblick |
| Risikomodell | Schadensszenarien | Schutzziele | Schutzbedarf |
| Strukturtiefe | hoch (sehr granular) | hoch (rechtlich praezise) | mittel (technikfokus) |
| Aufsichtsakzeptanz DE | gut | sehr gut | gut bei TOM |
| Aufsichtsakzeptanz FR | sehr gut | -- | -- |
| Eignung KI-Systeme | gut | sehr gut (Schutzziele) | begrenzt |
| Eignung TOM Art. 32 | mittel | gut | sehr gut |

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Was wird verarbeitet, wer ist Verantwortlicher, in welcher Jurisdiktion?
2. **Verhältnismäßigkeitspruefung.** Welche Methodik passt zur Verarbeitung? Standortbezug DE: SDM bevorzugt; FR-Bezug: CNIL PIA; reine TOM-Fragen: BSI-Bausteine ergaenzend.
3. **Risikoanalyse.** Methodisches Risikomodell waehlen: Schadensszenarien (CNIL), Schutzziele (SDM) oder Schutzbedarf (BSI).
4. **Maßnahmen.** Methode steuert die Maßnahmenstruktur: CNIL fragt pro Szenario, SDM pro Schutzziel, BSI pro Baustein.
5. **Restrisiko.** Methodenwahl beeinflusst Bewertungsmaßstab; bei Hybridansatz beide Skalen dokumentieren.
6. **Konsultation / Genehmigung.** DSB-Anhörung; Methodenwahl in der DSFA explizit begruenden.

## Mustertext / Template (Methodenwahl-Memo)

```
METHODENWAHL DSFA [DATUM]

Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME] | Sitzland: [DE/FR/...]

1. Methodenkandidaten
- CNIL PIA Software (Version [X], Sprache [DE/EN/FR])
- Standard-Datenschutzmodell SDM (Version V3.0)
- BSI-Grundschutz Datenschutz-Baustein

2. Bewertung
- Aufsichtsakzeptanz: [Begruendung]
- Werkzeugverfuegbarkeit: [Lizenz, Sprache, Schulung]
- Eignung Risikotyp: [...]
- Eignung TOM: [...]

3. Methodenwahl
[ ] CNIL PIA (Software-gestuetzt, modular, Schadensszenarien)
[ ] SDM (Schutzziele, DE-Aufsicht, KI-tauglich)
[ ] BSI ergaenzend für TOM Art. 32
[ ] Hybrid: SDM-Hauptmethodik plus BSI für TOM

4. Begruendung
[Warum diese Methode für diese Verarbeitung]

5. Werkzeug
- CNIL: cnil.fr/de/das-pia-tool-software-die-die-durchfuehrung-von-datenschutz
- SDM: datenschutzkonferenz-online.de/standard-datenschutzmodell.html
- BSI: bsi.bund.de/grundschutz

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________
```

## Werkzeug-Hinweise zur Auswahl

- CNIL PIA Software: kostenfrei, Open Source, mehrsprachig (DE-Lokalisierung verfuegbar), Export PDF und XML.
- SDM V3.0: Methodenbeschreibung der DSK, frei verfuegbar, keine Software, sondern Prüfkatalog.
- BSI-Grundschutz: Fachüberblick mit Bausteinen, GSTOOL bzw. verinice als Werkzeug.
- Hybridansatz Empfehlung: SDM als methodische Klammer, CNIL PIA Software für strukturierte Risikoszenarien, BSI für TOM nach Art. 32 DSGVO.

## Anwendungsfaelle

- KI-System mit Profiling: SDM bevorzugt, weil Schutzziele die KI-typischen Risiken (Transparenz, Nicht-Verkettung) sauber adressieren.
- Cloud-Migration mit US-Anbieter: CNIL PIA Software für Risikoszenarien plus BSI-Bausteine für technische Schutzmassnahmen.
- Beschäftigtenverarbeitung mit Mitbestimmung: SDM mit ergaenzendem Stakeholder-Modul.
- Forschungsverarbeitung mit besonderen Kategorien: SDM und CNIL PIA kombinieren; Beweislast-Aspekt nach Art. 5 Abs. 2 DSGVO mitfuehren.

## Typische Fehler

- Methode wird nicht explizit gewaehlt — Aufsicht verlangt Begruendung.
- CNIL PIA wird wegen schoener Software gewaehlt, ohne dass die Schutzziele DE adressiert werden.
- BSI-Grundschutz wird als DSFA-Ersatz behandelt — er ist primaer Sicherheitsmethodik.
- Hybridansatz wird gewaehlt, ohne die Schnittstellen zu definieren — Doppelarbeit oder Luecken.
- Sprache der Methodenartefakte passt nicht zur Aufsicht (CNIL-Output franzoesisch bei deutscher Aufsicht).
- Methodenwahl wird im Projektverlauf gewechselt — kein Quervergleich der Risikobewertung mehr möglich.
- Aufsichtshinweise zur Methodenfreiheit werden als Beliebigkeit verstanden — die Methode muss zur Verarbeitung passen.

## Quellen Stand 06/2026

- Art. 35 Abs. 7 DSGVO
- EDSA-Leitlinien WP 248 rev.01
- CNIL: cnil.fr — PIA Software, Knowledge Base, Methodology, Templates
- DSK Datenschutzkonferenz: datenschutzkonferenz-online.de — SDM V3.0
- BSI: bsi.bund.de — Grundschutz-Fachüberblick, Baustein zum Datenschutz
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle
