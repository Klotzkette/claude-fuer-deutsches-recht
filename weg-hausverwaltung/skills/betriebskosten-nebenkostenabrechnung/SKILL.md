---
name: betriebskosten-nebenkostenabrechnung
description: "Kontrolliert Betriebskosten- und Nebenkostenabrechnungen im Hausverwaltungs- und Vermietungskontext (Stand 05/2026): BetrKV, HeizkostenV, Mietvertrag, WEG-Abrechnung, Umlagefähigkeit, Abrechnungsfrist § 556 Abs. 3 BGB, Verteilerschlüssel, Belege, Einwendungen, CO2KostAufG-Aufteilung und Mietpreisbremse-Schnittstelle (BGBl. 2025 I Nr. 163)."
---

# Betriebskosten und Nebenkosten

Stand: 05/2026.

## Ziel

Die Schnittstelle zwischen WEG-Jahresabrechnung und mietrechtlicher Betriebskostenabrechnung sauber beherrschen.

## Prüfung

- **Umlagefähigkeit** nach Mietvertrag (Klausel auf BetrKV verweisend) und BetrKV (https://www.gesetze-im-internet.de/betrkv/).
- **Abrechnungszeitraum**: in der Regel Kalenderjahr; muss im Mietvertrag oder konsequent praktiziert sein.
- **Zugangsfrist**: Vermieter muss innerhalb von **12 Monaten** ab Ende des Abrechnungszeitraums abrechnen (§ 556 Abs. 3 BGB — https://www.gesetze-im-internet.de/bgb/__556.html). Nach Ablauf nur noch zugunsten des Mieters Korrekturen möglich.
- **Verteilerschlüssel** nach Mietvertrag, Wohnfläche, Verbrauch oder Einheiten; Heizung/Warmwasser zwingend mindestens 50/30/70 Prozent nach Verbrauch (HeizkostenV).
- **HeizkostenV**: Erfassung, Verteilung, Ablesung, Zwischenablesung bei Mieterwechsel.
- **Nicht umlagefähig**: Verwaltungskosten, Instandsetzung/Erhaltung (vs. Wartung), Bankgebühren ohne Vertragsgrundlage, Reparaturen, Erhaltungsrücklage.
- **Belegeinsicht** nach Aufforderung; Vermieter muss Einsicht ermöglichen, ggf. gegen Kostenerstattung Kopien.
- **Einwendungen** des Mieters: innerhalb 12 Monaten ab Zugang der Abrechnung (§ 556 Abs. 3 Satz 5 BGB).

## CO2KostAufG (seit 01.01.2023)

- Verteilung der CO₂-Kosten zwischen Vermieter und Mieter nach Zehn-Stufen-Modell (kg CO₂/m²·a).
- Hoch-Emissionsgebäude: Vermieter trägt 95 %, Mieter 5 %. EH-55-Neubau: Mieter 100 %.
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

## Cross-Refs

- WEG-Abrechnungsseite → `wirtschaftsplan-jahresabrechnung-28-weg`
- Vermietender Eigentümer / Datenfluss → `verwalterpflichten-26-27-weg`
- Eskalation → `eskalation-anwalt-amtsgericht`
- Mietrecht-Plugin als Schnittstelle

## Quellenpflicht

`rechtsstand-mai-2026-faktenbank` laden. BetrKV: https://www.gesetze-im-internet.de/betrkv/ ; HeizkostenV: https://www.gesetze-im-internet.de/heizkostenv/ ; § 556 BGB: https://www.gesetze-im-internet.de/bgb/__556.html .
