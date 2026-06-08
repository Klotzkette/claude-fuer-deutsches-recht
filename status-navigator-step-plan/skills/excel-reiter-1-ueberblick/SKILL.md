---
name: excel-reiter-1-ueberblick
description: "Baut Reiter 1 der Step-Plan-Excel: Ueberblick aller fuer die Durchsetzung erforderlichen Dokumente. Spalten Dokument, Datum, Verfuegbarkeit, Unterschriftsstatus, Unterzeichnet von (Partei und Funktion), Rechtsgrundlage (Klausel im zugrunde liegenden Vertrag) und Zweck. Mit Ampelfaerbung und Sortierung nach Vertragsebene."
---

# Reiter 1 Ueberblick Statuslage

## Rolle und Fokus
Reiter 1 ist die Gesamtsituation auf einen Blick. Alle fuer die Durchsetzung erforderlichen Dokumente in einer Zeile mit den wichtigsten Statusfeldern.

## Vorgehen

1. **Pflichtspalten setzen** — Dokument, Datum, Verfuegbarkeit, Unterschriftsstatus, Unterzeichnet von (Partei und Funktion), Rechtsgrundlage (Klausel), Zweck, Empfaenger, Versand-/Zustellungsstatus.
2. **Sortierung nach Vertragsebene** — Pachtvertrag-Cluster, Finanzierungs-Cluster, Genehmigungs-Cluster, Sicherheiten-Cluster.
3. **Verfuegbarkeit mit drei Werten** — `vorliegend`, `teilweise`, `fehlt`.
4. **Ampel auf Status-Spalten** — bedingte Formatierung gemaess `ampel-system`.
5. **Spalte Querverweis** — Jeder Eintrag verweist auf detaillierte Pruefspur in Reiter 2/3/4.

## Anwendungsbeispiel
LausitzStorage Reiter 1: 28 Zeilen ueber 4 Cluster, davon 4 rot (NordCap-Drawstop-Schreiben Zugang, Anlage 4 Konsortial, BImSchG-Vorbescheid Auflagen, Avalstatus 50Hertz), 7 gelb (Cap-Table-Versionen, drei Unterschriftsbefunde, ein Beschluss-Formfrage), Rest gruen. Pro Cluster eine Subsumtionszeile mit Cluster-Gesamtstatus.

## Output-Module
- Reiter 1 als Master-Index mit Querverweis in jede Detailpruefung
- Cluster-Gesamtstatuszeile je Vertragsebene
- Spalte Querverweis zu Reiter 2/3/4
