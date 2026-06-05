---
name: local-counsel-loeschung-erwiderung
description: "Local Counsel Loeschung Erwiderung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Local Counsel Loeschung Erwiderung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Local Counsel Loeschung Erwiderung** im Plugin Gebrauchsmusterrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `local-counsel-briefing-ausland` | Local-Counsel-Briefing für ausländische Utility-Model-Fragen erstellen: technische Lehre, Priorität, Offenbarung, Produkt, Gegner und gewünschte Maßnahme. |
| `loeschung-erwiderung-inhaber` | Erwiderung des Inhabers im Löschungsverfahren: Verteidigung, Hilfsanträge, Beschränkung, Belege und Vergleichsoptionen. |

## Arbeitsweg

Im Plugin Gebrauchsmusterrecht gilt für **Local Counsel Loeschung Erwiderung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `local-counsel-briefing-ausland`

**Fokus:** Local-Counsel-Briefing für ausländische Utility-Model-Fragen erstellen: technische Lehre, Priorität, Offenbarung, Produkt, Gegner und gewünschte Maßnahme.

# Local Counsel Briefing Ausland

## Wann dieser Skill hilft

Ein ausländischer Anwalt soll eingebunden werden.

## Arbeitsweise

Stelle präzise Fragen statt pauschaler Rechtsaufträge.

## Prüfpunkte

- Sachverhalt und Rolle sauber erfassen: Wer handelt, wer ist Rechteinhaber, wer ist Gegner, welches Produkt oder welche Kollektion ist betroffen?
- Fristen, Registerstand, Veröffentlichungen, Vertragslage und Beweisunterlagen früh sichern.
- Materielle Prüfung und Verfahrensstrategie trennen: Ein gutes Ergebnis sagt nicht nur, ob etwas möglich ist, sondern wie man es belegt, vorbereitet und durchsetzt.
- Unsichere Tatsachen offen markieren und mit präzisen Rückfragen schließen.

## Output

Counsel-Briefing.

## Quellen-Hardening

- Normen, Amtsinformationen, Registerdaten, Formulare, Gebühren und Fristen vor belastbarer Ausgabe live in den offiziellen Quellen prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und amtlicher oder frei zugänglicher Quelle verwenden.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Ausländisches Recht nur als Struktur, Risiko- und Local-Counsel-Briefing ausgeben, wenn keine aktuelle lokale Prüfung vorliegt.

## 2. `loeschung-erwiderung-inhaber`

**Fokus:** Erwiderung des Inhabers im Löschungsverfahren: Verteidigung, Hilfsanträge, Beschränkung, Belege und Vergleichsoptionen.

# Loeschung Erwiderung Inhaber

## Wann dieser Skill hilft

Ein Löschungsantrag liegt vor.

## Arbeitsweise

Prüfe Teilverteidigung und beschränkte Anspruchsfassung.

## Prüfpunkte

- Sachverhalt und Rolle sauber erfassen: Wer handelt, wer ist Rechteinhaber, wer ist Gegner, welches Produkt oder welche Kollektion ist betroffen?
- Fristen, Registerstand, Veröffentlichungen, Vertragslage und Beweisunterlagen früh sichern.
- Materielle Prüfung und Verfahrensstrategie trennen: Ein gutes Ergebnis sagt nicht nur, ob etwas möglich ist, sondern wie man es belegt, vorbereitet und durchsetzt.
- Unsichere Tatsachen offen markieren und mit präzisen Rückfragen schließen.

## Konkrete Norm-Anker

### Verfahrensgang
- **§ 17 GebrMG**: Loeschungsantrag wird dem Inhaber zugestellt.
- Inhaber hat **1 Monat Widerspruchsfrist**.
- Bei Schweigen Loeschung kraft Saeumnis (Default-Loeschung).

### Erwiderungsinhalt
1. **Widerspruch**: ausdruecklich erklaeren.
2. **Sachvortrag**: Antwort auf jeden Loeschungsgrund.
3. **Beweismittel**: Stand der Technik gegenrecherchieren, Hilfsantraege formulieren.
4. **Hilfsantraege**: praezisierte Schutzansprueche (Beschraenkung).

### Hilfsantraege (§ 16 Abs. 1 Satz 2 GebrMG iVm § 17 GebrMG)
- Praezisierung durch Aufnahme abhaengiger Anspruchsmerkmale.
- Streichung von Alternativen.
- Beschraenkung des Schutzbereichs.

### Praxistipp
- Frueher Hilfsantraege formulieren, um Teilloeschung zu vermeiden.
- Skill `teilloeschung-und-hilfsantraege` als Schwester-Skill heranziehen.

### Schwerpunkt
- Wenn ein Loeschungsantrag gegen das eigene Gebrauchsmuster geht, ist die Frist von 1 Monat sehr kurz.
- Anwaltliche Eile geboten.

## Output

Erwiderungsplan.

## Quellen-Hardening

- Normen, Amtsinformationen, Registerdaten, Formulare, Gebühren und Fristen vor belastbarer Ausgabe live in den offiziellen Quellen prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und amtlicher oder frei zugänglicher Quelle verwenden.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Ausländisches Recht nur als Struktur, Risiko- und Local-Counsel-Briefing ausgeben, wenn keine aktuelle lokale Prüfung vorliegt.
