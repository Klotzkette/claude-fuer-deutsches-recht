---
name: urheberrecht-bausteine
description: "Urheberrechtliche Bausteine fuer KI-Nutzungsrichtlinien in Kanzleien: Anwendungsfall Kanzlei will wissen ob KI-generierte Texte urheberrechtlich schuetzbar sind und welche Texte als Eingabe hochgeladen werden duerfen. § 2 Abs. 2 UrhG geistige Schoepfung, § 5 UrhG amtliche Werke, juris und beck-online Lizenzbedingungen. Pruefraster kein Urheberrechtsschutz fuer reine KI-Outputs, Upload-Verbote urheberrechtlich geschuetzter Texte, Trainer-Klauseln der Anbieter. Output Urheberrechts-Bausteine fuer Kanzlei-Richtlinie mit Upload-Verbotsliste. Abgrenzung zu Kennzeichnungspflichten und zu Dienstleister-Due-Diligence."
---

# Urheberrecht-Bausteine

Der urheberrechtliche Status von KI-generierten Inhalten und die Frage, welche Texte in KI-Systeme hochgeladen werden dürfen, sind in Kanzleien von erheblicher praktischer Bedeutung. Dieser Skill stellt die relevanten urheberrechtlichen Bausteine zusammen und gibt konkrete Handlungsempfehlungen.

## Rechtlicher Hintergrund

§ 2 Abs. 2 UrhG: Urheberrechtlicher Schutz nur für „persönliche geistige Schöpfungen" — rein maschinell erzeugter Output von KI-Systemen genießt in der Regel keinen urheberrechtlichen Schutz. § 5 UrhG: Amtliche Werke (Gesetze, Verordnungen, gerichtliche Entscheidungen) sind gemeinfrei und dürfen ohne Einschränkung genutzt werden. §§ 44a ff. UrhG: Urheberrechtsschranken (Privatkopie, wissenschaftliche Nutzung, Text- und Data-Mining nach § 44b UrhG). § 87a UrhG: Datenbankherstellerschutz für proprietäre Rechtsdatenbanken wie juris oder beck-online. § 31 UrhG: Nutzungsrechtsübertragung — maßgeblich für Lizenzbedingungen der Datenbankanbieter.

## Vorgehen

1. **Status des KI-Outputs bestimmen**: KI-generierter Text ohne menschlichen Schöpfungsanteil ist urheberrechtlich nicht geschützt. Erst bei maßgeblichem menschlichen Schöpfungsbeitrag (qualifizierter Prompt mit Schöpfungshöhe + inhaltliche Bearbeitung) entsteht ein Schutzrecht.
2. **Upload urheberrechtlich geschützter Texte prüfen**: Juristische Aufsätze, Kommentare, Fachbuchkapitel dürfen nur hochgeladen werden, wenn eine Nutzungslizenz vorliegt.
3. **Amtliche Werke nutzen**: Gerichtsentscheidungen von offiziellen Gerichts-Websites und Gesetzestexte sind gemeinfrei nach § 5 UrhG — Upload unkritisch.
4. **Vorsicht bei Datenbankimporten**: Aus juris oder beck-online entnommene Texte können Datenbankschutz (§ 87b UrhG) und zusätzliche Lizenzklauseln der Anbieter auslösen; AGB der Datenbanken prüfen.
5. **Anonymisierung bei Urteilen beachten**: Auch gemeinfreie Urteile enthalten ggf. personenbezogene Daten; auf ordnungsgemäße Pseudonymisierung achten.
6. **Trainingsklauseln des Anbieters prüfen**: Viele KI-Anbieter nutzen hochgeladene Dokumente zum Training ihrer Modelle; Opt-out-Optionen vertraglich absichern (vgl. Skill `dienstleister-due-diligence`).

## Vorlagentext / Bausteine

**Baustein Urheberrecht KI-Output:**
Der durch KI-Systeme generierte Text stellt in der Regel keine persönliche geistige Schöpfung im Sinne des § 2 Abs. 2 UrhG dar und ist damit urheberrechtlich nicht geschützt. Mitarbeitende sollten sich nicht darauf verlassen, dass KI-generierte Inhalte allein deshalb frei von Drittrechten sind — das KI-System kann urheberrechtlich geschütztes Material aus seinem Training reproduzieren. Jeder extern verwendete KI-generierte Text ist daher auf mögliche Rechtsverletzungen zu prüfen.

**Baustein Upload-Beschränkungen:**
In KI-Systeme dürfen nur solche Texte und Dokumente hochgeladen werden, für die die Kanzlei über die erforderlichen Nutzungsrechte verfügt. Juristische Kommentare, Fachaufsätze und Datenbankexporte unterliegen regelmäßig Urheberrechtsschutz und Lizenzklauseln. Amtliche Werke nach § 5 UrhG (Gesetzestexte, Verordnungen, Gerichtsentscheidungen auf offiziellen Portalen) sind gemeinfrei und dürfen uneingeschränkt genutzt werden.

**Baustein Datenbanken:**
Bei der Verwendung von Texten aus juristischen Fachdatenbanken (juris, beck-online, Wolters Kluwer u.a.) sind die jeweiligen AGB und Lizenzvereinbarungen zu beachten. Diese Anbieter verfügen über Datenbankherstellerschutz nach § 87a UrhG. Vor dem Upload von Datenbankexporten in KI-Systeme ist die ausdrückliche Erlaubnis des Datenbankbetreibers einzuholen oder es sind ausschließlich amtliche Quellen zu verwenden.

## Hinweise zur Aktualisierung

Das Urheberrecht im Bereich KI entwickelt sich rasch weiter — insbesondere durch laufende Gerichtsverfahren in den USA (z.B. zu fair use beim Training von KI-Systemen) und mögliche europäische Gesetzgebung. Zudem passen juris und beck-online ihre AGB gelegentlich an. Halbjährlich prüfen, ob Aktualisierungen erforderlich sind.

## Aktuelle Rechtsprechung (v14.2)
- BGH, Urt. v. 27.04.2017 — I ZR 55/16, NJW 2017, 3304 Rn. 22: Urheberrecht erfordert persoenliche geistige Schoepfung § 2 Abs. 2 UrhG — KI-generierte Werke ohne menschliche Kreativitaet nicht schuetzbar.
- EuGH, Urt. v. 04.10.2011 — C-403/08 (FAPL), NJW 2012, 126 Rn. 98: Werksqualitaet erfordert Ausdruck menschlicher Kreativitaet — massgeblich fuer KI-Output-Schutzfrage.
- BGH, Urt. v. 17.07.2013 — I ZR 129/08 (UsedSoft II), NJW 2013, 3309 Rn. 28: Erschoepfungsgrundsatz bei digitalen Produkten — relevant fuer KI-Trainingsdaten aus lizenzierten Quellen.
- EuGH, Urt. v. 12.09.2019 — C-683/17 (Cofemel), NJW 2019, 3218 Rn. 30: Einheitlicher EU-Werkbegriff erfordert menschliche Schoepfungshoehe.

## Zentrale Normen (Paragrafenkette)
- § 2 Abs. 2 UrhG — Persoenliche geistige Schoepfung (KI-Output faellt nicht darunter)
- § 44b UrhG — Text-und-Data-Mining-Schranke (Opt-out-Vorbehalt)
- Art. 4 DSM-RL (EU 2019/790) — Text-und-Data-Mining fuer KI-Training
- § 97 UrhG — Schadensersatz bei Urheberrechtsverletzung durch Trainingsdaten
- § 72 UrhG — Lichtbildschutz (grenz zur KI-generierten Bildkreation)

## Triage zu Beginn
1. Wer hat das Urheberrecht an KI-generierten Texten — Anwalt, KI-Anbieter, oder niemand?
2. Werden urheberrechtlich geschuetzte Werke als Trainingsdaten verwendet — § 44b UrhG pruefen?
3. Hat der Anbieter einen Text-und-Data-Mining-Opt-out erklaert (Art. 4 DSM-RL)?
4. Werden KI-Outputs an Mandanten uebermittelt — wer haftet bei Urheberrechtsverletzung?
5. Sind Fotos oder Bilder Teil der KI-Nutzung — gilt § 72 UrhG oder KI-Bildrecht-Luecke?

## Output-Template — Urheberrechts-Baustein KI-Richtlinie
**Adressat:** Kanzlei / Rechtsabteilung — Tonfall: rechtlich, praezise
```
URHEBERRECHTS-BAUSTEIN
Fuer: KI-Nutzungsrichtlinie [KANZLEI] — Stand: [DATUM]

§ [X] URHEBERRECHT UND KI-GENERIERTE INHALTE

(1) Schutzfaehigkeit: KI-generierte Texte, Bilder und sonstige Inhalte sind
ohne hinreichende menschliche Gestaltung nicht urheberrechtlich geschuetzt
(§ 2 Abs. 2 UrhG). Die Kanzlei erhaelt kein Urheberrecht an reinen KI-Outputs.

(2) Trainingsdaten: KI-Systeme duerfen nur mit Trainingsdaten betrieben werden,
fuer die die Nutzungsrechte vorliegen oder die unter § 44b UrhG fallen.

(3) Fremdinhalte in Prompts: Das Einlesen urheberrechtlich geschuetzter Drittwerke
in KI-Systeme ist nur zulaessig, wenn kein Opt-out nach Art. 4 DSM-RL erklaert
wurde und die Nutzung dem Zweck des § 44b UrhG entspricht.

(4) Haftung: Bei Verdacht auf Urheberrechtsverletzung durch KI-Output ist
unverzueglich [ANSPRECHPARTNER] zu informieren.
```
