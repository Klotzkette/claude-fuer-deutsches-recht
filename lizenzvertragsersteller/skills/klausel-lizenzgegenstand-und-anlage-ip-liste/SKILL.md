---
name: klausel-lizenzgegenstand-und-anlage-ip-liste
description: "Klausel Lizenzgegenstand mit Anlage A (IP-Liste): pro IP-Typ Identifikation, Schutzrechtsregister-Nummern, Schutzgebiete, Lebensdauer, Belastungen; mit Praezisierungstechniken (Patente per Anspruch, Marken per Nizza-Klasse, Software per Repository-Hash)."
---

# Klausel Lizenzgegenstand + Anlage A

## Funktion

Praezision schlaegt Generalformulierung. Wer den Lizenzgegenstand vage haelt ("alle IP, die der Lizenzgeber besitzt"), riskiert später Streit über Zugehoerigkeit.

## Praezisierungstechniken pro IP-Typ

| IP-Typ | Identifikation |
|---|---|
| Urheberrecht (Werk) | Titel, Schoepfer, Schoepfungsjahr, Werkkategorie |
| Software | Repository-URL, Commit-Hash (z. B. SHA), Branch-Name, Build-Version |
| Patent | Reg.-Nr. + Datum + ggf. Anspruchsnummer |
| Marke | Reg.-Nr., Wortmarke/Bildmarke, Nizza-Klassen |
| Design | Reg.-Nr., Beschreibung, Schutzgebiete |
| Gebrauchsmuster | Reg.-Nr., Datum |
| Geschäftsgeheimnis | Bezeichnung + Anlage-Hash + Versionsnummer |
| Domain | Domain + Registrar |

## Anlage-A-Schema (Standard)

```
ANLAGE A — LIZENZGEGENSTAND
==========================

A.1 Patente

| Nr. | Reg.-Nr. | Schutzgebiet | Anmeldedatum | Status | Erfinder | Lizenzansprueche |
|-----|----------|--------------|--------------|--------|----------|-------------------|

A.2 Marken

| Nr. | Reg.-Nr. | Wort/Bild | Nizza-Klassen | Schutzgebiete | Verlaengerung | Status |
|-----|----------|-----------|---------------|---------------|---------------|--------|

A.3 Software

| Nr. | Repository | Commit-Hash | Branch | Build-Version | Vergebene Sublizenzen |
|-----|-----------|-------------|--------|---------------|----------------------|

A.4 Know-how

| Nr. | Bezeichnung | Anlage-Hash | Versionsnummer | Schutzmassnahmen |
|-----|-------------|-------------|----------------|------------------|
```

## Klausel-Baustein

> **$ 2 Lizenzgegenstand.**
>
> (1) Lizenzgegenstand sind die in **Anlage A** aufgefuehrten Schutzrechte und das in Anlage A definierte Know-how (gemeinsam "Lizenzgegenstand").
>
> (2) Etwaige Anspruchserweiterungen, Patentanmeldungen aus derselben Erfindung oder Folgeanmeldungen fallen [JA / NEIN] automatisch unter den Lizenzgegenstand. Bei JA: Aktualisierung Anlage A jaehrlich.
>
> (3) Anlage A ist integraler Bestandteil dieses Vertrages.

## Prüfroutine vor Vertragsschluss

1. Schutzrechtsregister live abfragen (DPMA, EUIPO, EPA)
2. Whois für Domains
3. Repository-Hash bei Software (z. B. `git log -1 --pretty="%H"`)
4. Anlage-Hash bei Know-how (SHA-256 der Dokumentensammlung)
5. Belastungen pro Schutzrecht eintragen

## Anschluss

- IP-Identifikation: `ip-identifikation-und-bestandsaufnahme`
- Lizenzumfang: `klausel-lizenzumfang-territorium-zeit-feld`
