---
name: unterlagen-luecken
description: "Auf Bieterseite: Lücken- und Beschaffungsliste für Vergaberecht: trennt fehlende Tatsachen von fehlenden Belegen (Vergabeunterlagen, Angebot, Wertungsvermerk), nennt pro Lücke Beweisthema, Beschaffungsweg (Vergabekammer Bund/Länder), Frist und Ersatznachweis."
---

# Unterlagen und Lücken

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Einsatzlage

Diese Unterlagenprüfung für Vergaberecht benennt fehlende Dokumente, streitige Tatsachen, Beweisrisiken und die kürzeste sichere Nachforderung.

## Fachlandkarte dieses Plugins

- `dokumente-intake` — Aktenstart und Unterlageninventar.
- `workflow-unterlagen-lueckenliste` — fehlende Unterlagen, Nachweise und Belege als Arbeitsauftrag.
- `unterlagen-und-lv-datenformate-auslesen` — LV, GAEB, XML, Excel, PDF und Portalformulare prüfen.
- `angebot-in-vorgegebenem-format-erstellen` — Angebotsabgabe und Uploadpaket vorbereiten.
- `bieterfragen-antworten-management` — Klärungsfrage und Fristverlängerung vor Rüge.
- `21-ruegeschreiben-erstellen` — rügepflichtige Unterlagenlücke rechtzeitig angreifen.
- `nachpruefungsantrag-powerdraft` und `nachpruefungsverfahren-vk` — Nichtabhilfe und VK-Reserve.
- `eignungspruefung`, `ausschluss-bieter-paragraf-124-gwb` und `28-selbstreinigung-nach-ausschluss-paragraf-125` — Eignungs-/Ausschlusslücken.
- `08-bietergemeinschaft-bildung` und `17-bietergemeinschaftserklaerung` — BG-Nachweise, Steuer-/Sozialabgabenstatus und Mitgliederaustausch.

## Arbeitsweg

- Sollkatalog aufstellen: Welche Dokumente brauche ich für die konkrete Vergaberecht-Frage zwingend (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets)?
- Ist-Abgleich: Welche Dokumente sind vorhanden, welche fehlen, welche sind unvollständig, undatiert oder ohne Unterschrift?
- Lückenliste priorisieren nach: fristrelevant (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), beweisrelevant, formerheblich.
- Rückfrageschreiben an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen entwerfen — Wer hat das Dokument, woher kann es beschafft werden, bis wann?
- Bei behördlichen Lücken: Akteneinsichtsrecht (z. B. § 29 VwVfG, § 147 StPO, § 25 SGB X) prüfen und nutzen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
