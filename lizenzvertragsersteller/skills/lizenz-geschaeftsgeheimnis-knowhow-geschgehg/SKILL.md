---
name: lizenz-geschaeftsgeheimnis-knowhow-geschgehg
description: "Lizenz von Geschäftsgeheimnissen und Know-how nach GeschGehG: $$ 1-12 GeschGehG; Schutzmassnahmen $ 2 Nr. 1b; Reverse Engineering $ 3; Sphaeren-Trennung; Know-how-Lizenz mit Vertraulichkeitsklauseln und Sanktionsregelungen."
---

# Lizenz Geschäftsgeheimnis / Know-how (GeschGehG)

## Normenanker

- $ 1 GeschGehG - Schutzgegenstand
- $ 2 GeschGehG - Begriffsbestimmungen; $ 2 Nr. 1: Geschäftsgeheimnis = vertrauliche Information mit Schutzmassnahmen und wirtschaftlichem Wert
- $ 3 GeschGehG - Erlaubte Handlungen (Reverse Engineering bei rechtmaessig erlangter Sache!)
- $ 4 GeschGehG - Verbotene Handlungen
- $ 5 GeschGehG - Schutzausnahmen (Whistleblowing, Journalistik, Aufdeckung Fehlverhalten)
- $$ 6-12 GeschGehG - Rechtsfolgen (Unterlassung, Schadensersatz, Auskunft, Vernichtung)

## Pflichtbaustein: Schutzmassnahmen vor Lizenz

Damit Know-how als Geschäftsgeheimnis schutzfaehig bleibt, muss der Lizenzgeber vor Vertragsschluss nachweisen, dass:

1. **Zugriffsbeschraenkungen** - Need-to-Know, MFA, Branch Protection
2. **NDAs** mit Mitarbeitern, Beratern, Sub-Unternehmern
3. **Dokumentation** der Schutzmassnahmen
4. **Technische Sicherungen** (Verschluesselung, Audit-Trail)

Ohne Schutzmassnahmen kein Geheimnis, kein Schutz, keine durchsetzbare Lizenz.

## Reverse Engineering — Sonderfall

$ 3 GeschGehG: Reverse Engineering einer rechtmaessig erlangten Sache ist **erlaubt**, soweit der Inhaber das nicht vertraglich ausgeschlossen hat.

→ Im Lizenzvertrag: **Reverse-Engineering-Verbot** ausdruecklich vereinbaren ($ 3 Abs. 2 GeschGehG).

## Lizenztypen

| Typ | Inhalt |
|---|---|
| Know-how-Lizenz | Berechtigung zur Nutzung vertraulicher Informationen + Schulungspflicht des Lizenzgebers |
| Mixed Lizenz | Know-how + Patent + Marke kombiniert (TT-GVO-relevant) |
| NDA-Lizenz | reine Geheimhaltungsverpflichtung ohne Nutzungsrecht (selten - eher pre-License) |

## Klausel-Bausteine (DE)

**1. Lizenzgegenstand Geschäftsgeheimnis:**
> "Der Lizenzgeber raeumt dem Lizenznehmer hiermit das nicht-ausschliessliche, nicht-uebertragbare Recht ein, das in **Anlage A** bezeichnete Know-how ("Lizenz-Know-how") für die in **Anlage B** definierten Zwecke zu nutzen. Das Lizenz-Know-how umfasst die in Anlage A aufgefuehrten technischen Unterlagen, Daten, Prozessbeschreibungen und Quellcode-Auszuege."

**2. Vertraulichkeitspflicht:**
> "Der Lizenznehmer verpflichtet sich, das Lizenz-Know-how mit der Sorgfalt eines ordentlichen Kaufmanns geheim zu halten. Insbesondere wird der Lizenznehmer (i) Zugriff auf das Need-to-Know-Prinzip beschraenken, (ii) Mitarbeitern und Beratern entsprechende Geheimhaltungsvereinbarungen auferlegen, (iii) das Lizenz-Know-how durch technische Maßnahmen sichern und (iv) keine Kopien ausserhalb des Vertragsbereichs anfertigen."

**3. Reverse-Engineering-Verbot:**
> "Der Lizenznehmer wird das Lizenz-Know-how nicht reverse-engineeren, dekompilieren oder durch Analyse der Erscheinungsform Rueckschluesse auf seine Bestandteile ziehen. Dieses Verbot gilt im Sinne des $ 3 Abs. 2 GeschGehG."

**4. Rueckgabepflicht:**
> "Nach Vertragsbeendigung gibt der Lizenznehmer saemtliche schriftlichen und elektronischen Unterlagen des Lizenz-Know-hows binnen 30 Tagen zurueck oder vernichtet sie nachweislich; bestaetigt schriftlich gegenueber dem Lizenzgeber."

## Anschluss

- NDA für Vorvertrag: `klausel-vertraulichkeit-und-nda-interimsphase` (folgt)
- Insolvenz: `insolvenz-fortbestand-paragraf-103-inso-lizenz`
