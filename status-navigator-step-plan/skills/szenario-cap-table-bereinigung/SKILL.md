---
name: szenario-cap-table-bereinigung
description: "Anwendungsszenario Bereinigung mehrerer widerspruechlicher Cap Tables. Status-Navigator vergleicht die Cap Tables miteinander und mit den zugrundeliegenden Vertraegen. Zeigt Abweichungen und Wandlungsbedarf auf."
---

# Szenario Cap Table Bereinigung

## Rolle und Fokus
Bereinigung mehrerer widerspruechlicher Cap Tables. Status-Navigator vergleicht Cap Tables miteinander und mit den zugrundeliegenden Vertraegen.

## Vorgehen

1. **Versionsregister aufbauen** — Skill `dokumententyp-cap-tables` liefert pro Version eine normalisierte Tabelle.
2. **Abweichungen klassifizieren** — Tippfehler, fehlende Wandlung dokumentiert, materielle Anteilsverschiebung.
3. **Quellnachweis pro Anteil** — Welcher Vertrag, welcher Beschluss, welcher Notarakt begruendet die Position?
4. **Wandlungs- und Optionsereignisse pruefen** — Wandeldarlehen, ESOP, Vorzugswandlung — sind alle erfassbaren Ereignisse abgebildet?
5. **Konsolidierte Soll-Cap-Table** — Stichdatum, Quellgrundlage je Zeile, Abweichungs-Memo.

## Anwendungsbeispiel
LausitzStorage Cap-Table-Bereinigung: drei Versionen (siehe `diskrepanzen-aufdecken`) zeigen die NordCap-Schwankung 48/51/48 %. Pruefung ergibt: keine Wandlung dokumentiert; v2 stammt aus NordCap-Datenraum und enthielt einen Tippfehler bei Konsortium Stadtwerke-Cottbus-Anteil; v3 ist die fehlerbereinigte Investor-Update-Version. Empfehlung Soll-Cap-Table = v3 mit Vermerk.

## Output-Module
- Soll-Cap-Table mit Quellnachweis je Zeile
- Abweichungs-Memo zu den abweichenden Versionen
- Querverweis an Skill `dokumententyp-beschluesse` bei vermuteter Wandlung
