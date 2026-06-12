---
name: dokumententyp-beschluesse
description: "Erkennt Beschluesse: Gesellschafterbeschluesse, Aufsichtsratsbeschluesse, Hauptversammlungsbeschluesse, Vorstandsbeschluesse. Erfasst Beschlussdatum, beschliessende Organe, Beschlussgegenstand und Formerfordernis."
---

# Dokumententyp Gesellschafterbeschluesse

## Rolle und Fokus
Erkennt Beschlüsse als Dokumentenklasse. Gesellschafterbeschluss, Aufsichtsrats-, Hauptversammlungs-, Vorstandsbeschluss. Erfasst Beschlussdatum, beschliessende Organe, Beschlussgegenstand und Formerfordernis.

## Anwendungsbeispiel
Gesellschafterbeschluss vom 17.10.2025: Zustimmung zum Senior-Darlehensvertrag NordCap und zur Bestellung der Sicherheiten. Beschluss vorhanden, aber Schriftform statt Umlaufbeschluss mit Originalunterschriften aller Gesellschafter — Form steht in der GmbH-Satzung § 11 (verlangt notarielles Protokoll für Sicherheitenbestellung > 50 Mio EUR). Klärungsbedarf.

## Output-Module
- Eintrag in Reiter 2 mit Typ-Tag Beschluss
- Querverweis auf zustimmungspflichtige Verträge (Reiter 2 Anmerkungsspalte)
- Hinweisliste an `unterschriftspruefung` und ggf. Reiter 3 wenn Form fragwuerdig
