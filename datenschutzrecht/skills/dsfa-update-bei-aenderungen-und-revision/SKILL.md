---
name: dsfa-update-bei-aenderungen-und-revision
description: "Aktualisierung einer DSFA bei wesentlichen Aenderungen der Verarbeitung nach Art. 35 Abs. 11 DSGVO. Output: Revisionsplan mit Trigger-Liste Aenderungsanalyse Risikoreassessment und Versionshistorie."
---

# DSFA Update bei Aenderungen und Revision

## Zweck

Steuerung der Aktualisierung einer bestehenden DSFA bei wesentlichen Aenderungen der Verarbeitungstaetigkeit nach Art. 35 Abs. 11 DSGVO. Ergebnis ist ein Revisionsplan mit Trigger-Liste, Aenderungsanalyse, Risikoreassessment und Versionshistorie. Ziel ist, die DSFA als lebendes Dokument zu fuehren und nicht als Einmalvorgang.

## Wann dieses Modul hilft

- Bei Aenderung der Zwecke einer Verarbeitung
- Bei neuem Auftragsverarbeiter oder Sub-Auftragsverarbeiter
- Bei neuem Drittlandtransfer
- Bei neuer Technologie (KI-Modul, Biometrie)
- Bei neuer Datenkategorie oder neuem Betroffenenkreis
- Bei aktualisierter Rechtsprechung oder Aufsichtsbehoerdenpraxis
- Bei wesentlich erweiterter Datenmenge oder Aufbewahrungsfrist
- Bei Vorfall (Art. 33 Datenpanne) — Risikobewertung neu ueberpruefen

## Rechtlicher Rahmen

- Art. 35 Abs. 11 DSGVO: Der Verantwortliche fuehrt erforderlichenfalls eine Ueberpruefung durch, um zu bewerten, ob die Verarbeitung gemaess der DSFA durchgefuehrt wird; dies gilt zumindest, wenn sich das mit den Verarbeitungsvorgaengen verbundene Risiko aendert.
- Art. 5 Abs. 2 DSGVO Rechenschaftspflicht — Versionshistorie und Begruendung der Re-Pruefung.
- Art. 30 DSGVO Verarbeitungsverzeichnis — Aenderungen sind dort zu spiegeln.
- EDSA-Leitlinien WP 248 rev.01.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Aktuellen Stand der Verarbeitung erfassen und mit der dokumentierten DSFA-Version vergleichen.
2. **Verhaeltnismaessigkeitspruefung.** Aenderung wesentlich? Schwellenwerte:
 - Neue oder weggefallene Zweck
 - Neue Datenkategorie
 - Neue Empfaenger oder neuer Drittlandtransfer
 - Neue Technologie
 - Neue Aufbewahrungsfrist (> 50 Prozent Verlaengerung)
 - Aufsichtsbehoerden- oder Rechtsprechungsaenderung
3. **Risikoanalyse.** Erneute Risikoanalyse nach Methodik des urspruenglichen DSFA-Skills; Risikomatrix vor und nach erneuten Massnahmen.
4. **Massnahmen.** Pruefung, ob bestehende Massnahmen ausreichen oder ergaenzt werden muessen.
5. **Restrisiko.** Vergleich Restrisiko alt versus neu; ggf. neue Art. 36 Konsultation.
6. **Konsultation / Genehmigung.** DSB-Anhörung, Freigabe und Versionierung; alte Versionen archivieren, nicht loeschen.

## Mustertext / Template Revisionsplan

```
DSFA-REVISIONSPLAN [DATUM]

Verarbeitung: [BEZEICHNUNG]
DSFA-Version aktuell: [X.Y]
DSFA-Version neu: [X.Y+1]
Verantwortlicher: [NAME]

1. Aenderungsanlass
[ ] Zweckaenderung
[ ] Neue Datenkategorie
[ ] Neuer Empfaenger / Sub-AV
[ ] Neuer Drittlandtransfer
[ ] Neue Technologie (z. B. KI-Modul)
[ ] Aufbewahrungsfrist
[ ] Rechtsprechungs- / Aufsichtspraxis-Update
[ ] Vorfall (Art. 33 DSGVO)
[ ] Routine-Revision (Datum: [DATUM])

2. Aenderungsanalyse
[Konkrete Beschreibung der Aenderung im Vergleich zur Vorversion]

3. Auswirkungen auf Schwellwertanalyse
[ ] Schwellwert unveraendert
[ ] Schwellwert neu erreicht (z. B. neues EDSA-Kriterium)
[ ] Schwellwert entfallen (z. B. Anonymisierung)

4. Risikoreassessment
- Risiken neu identifiziert: [Liste]
- Risikomatrix aktualisiert: ja / nein
- Restrisiko aendert sich: ja / nein
- Vorab-Konsultation Art. 36 ggf. neu erforderlich: ja / nein

5. Massnahmen
[Liste der zusaetzlichen oder geaenderten Massnahmen]

6. Freigabe
- DSB-Anhörung: [Datum, Stellungnahme]
- Genehmigung Verantwortlicher: [Name, Datum]
- Aufsicht informiert (falls Art. 36): [Datum]
- Eintrag Verarbeitungsverzeichnis aktualisiert: [Datum]
- Naechste Routine-Revision: [DATUM]

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________

Versionshistorie
| Version | Datum | Aenderung | Autor | Freigabe |
| 1.0 | [...] | Erstfassung | [...] | [...] |
| 1.1 | [...] | [...] | [...] | [...] |
| 2.0 | [...] | [...] | [...] | [...] |
```

## Empfohlene Revisionsfrequenz

- Routine-Revision: einmal jaehrlich, dokumentiert auch wenn keine Aenderung
- Anlassbezogene Revision: unverzueglich nach Trigger
- KI-Verarbeitungen: alle 6 Monate (wegen Modell- und Datenaenderungen)
- Beschaeftigtenverarbeitungen bei BetrVG-Tatbestand: nach jeder Betriebsvereinbarung
- Drittlandtransfer: nach jedem Schrems-Folgeurteil oder EDSA-Update

## Typische Fehler

- DSFA wird einmal erstellt und nie aktualisiert — Verstoss gegen Art. 35 Abs. 11 DSGVO.
- Aenderungen werden im Original-Dokument ueberschrieben — Versionshistorie geht verloren.
- Routine-Revision wird unterlassen, weil sich nichts geaendert hat — ohne Dokumentation kein Nachweis.
- Trigger werden nicht in das Change-Management-Verfahren integriert.
- Nach Datenpanne (Art. 33) wird die DSFA nicht ueberprueft.
- KI-Modellupdate wird nicht als Trigger erkannt.

## Querverweise

- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Basisvorlage
- `datenschutzrecht/skills/dsfa-restrisiko-und-art-36-konsultation/SKILL.md` — Vorabkonsultation bei Aenderung
- `datenschutzrecht/skills/dsfa-dokumentation-und-rechenschaftspflicht-art-5-ii/SKILL.md` — Versionierung
- `datenschutzrecht/skills/datenpanne-meldung/SKILL.md` — Trigger Datenpanne
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 35 Abs. 11 DSGVO
- Art. 5 Abs. 2, Art. 30, Art. 33 DSGVO
- EDSA-Leitlinien WP 248 rev.01
- EDSA-Stellungnahme 28/2024 zu KI-Modellen (Update-Trigger)
- BfDI / Landesbehoerden — Verfahrenshinweise
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle
