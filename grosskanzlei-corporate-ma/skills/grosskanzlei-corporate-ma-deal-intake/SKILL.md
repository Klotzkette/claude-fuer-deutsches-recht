---
name: grosskanzlei-corporate-ma-deal-intake
description: "Neues M&A-Mandat aufnehmen und strukturieren: Anwendungsfall Partner oder Associate erhaelt Erstanfrage zu einer Transaktion und muss Deal-Profil, Rolle, Parteien, Zeitplan und Workstreams erfassen. §§ 3a RVG Honorar, § 43a BRAO Konflikt. Pruefraster Deal-Typ Buy-side/Sell-side/Carve-out, Zielgesellschaft, Transaktionsstruktur, Zeitplan, Budget-Ersteinschaetzung, Annahme-Check. Output Deal-Intake-Sheet mit Parteienregister, Dealtyp, Workstreams, initiales Budget und Fristen-Erstliste. Abgrenzung zu Kaltstart-Skill fuer Kanzleipraeferenzen und zu Matter-File fuer laufende Akte."
---

# Deal-Intake

## Zweck

Strukturiert neue Transaktionsmandate aus E-Mail, Teaser, NDA, Term Sheet, Teams-Message, Screenshot oder Datenraum-Einladung.

## Arbeitsmodus

- Parteien, Zielgesellschaft, Deal-Typ, Jurisdiktionen, Zeitplan, Vertraulichkeit und erste rote Flaggen extrahieren.
- Konfliktcheck, Sanktionen, Insider-/Clean-Room-Fragen und Mandatsumfang anstoßen.
- Fehlende Kerninformationen als kurze IRL anlegen.
- Akte und Deal-Namen vorschlagen.

## Rote Schwellen

- Keine Konfliktprüfung.
- Insiderinformation oder Marktgeruecht in offenem Kanal.
- Datenraumzugang ohne NDA oder Need-to-know.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/deal-intake-sheet.md
- assets/templates/matter-opening-checklist.md

## Triage — klaere beim Erstkontakt

1. Wer sind Verkaeufer und Kaeufer — natuerliche Person, GmbH, AG, ausl. Gesellschaft?
2. Was ist das Kaufobjekt — GmbH-Anteile, AG-Aktien, Asset-Portfolio, Immobilien, IP?
3. Welcher Transaktionsstatus — erster Kontakt, NDA, Term Sheet, LOI, fortgeschrittene Verhandlung?
4. Gibt es Insiderinformationen — boersennotierte Zielgesellschaft → MAR-Pflichten sofort pruefen
5. Welches Budget und welcher Zeitplan sind angegeben?

## Zentrale Rechtsgrundlagen

- § 43a Abs. 4 BRAO — Interessenkonfliktpruefung vor Mandatsannahme; Pflicht zur Conflicts-Pruefung
- §§ 10, 11 GwG — Sorgfaltspflichten bei Mandatsannahme; Identifizierung aller Parteien und wirtschaftlich Berechtigter
- Art. 7, 17 MAR — bei boersennotierter Zielgesellschaft: Insiderinformation und Ad-hoc-Pflicht sofort beachten
- §§ 17-18 GeschGehG — Vertraulichkeitspflicht; NDA muss vor Informationsaustausch vorliegen
- § 49b BRAO — Honorarvereinbarung: bei M&A-Mandaten auch Erfolgshonorar nach RVG moeglich; schriftliche Vereinbarung empfohlen

## Aktuelle Rechtsprechung

- BGH, Urt. v. 07.10.2021 - IX ZR 1/21, NJW 2022, 137 — Interessenkonflikt: Sozietaetswechsel eines Anwalts begruendet kein automatisches Mandatsverbot; massgeblich ist tatsaechliche Kenntnisbedrohung; fruehere Mandatsbeziehung muss dokumentiert werden
- BGH, Urt. v. 23.05.2000 - IX ZR 353/98, NJW 2000, 2815 — Mandatsannahme: Anwalt haftet fuer Fehler bei der Pruefung, ob ein Mandat rechtmaessig angenommen werden kann; Unterlassen der Conflicts-Pruefung kann Schadenersatz ausloesen

## Kommentarliteratur

- Schramm/Alexander, BRAO, § 43a Rn. 40-70 (Interessenkonflikt, Mandatsannahme)
- Gercke/Leimenstoll, GwG, §§ 10-11 Rn. 1-50 (Sorgfaltspflichten bei Mandatsannahme)

## Schritt-fuer-Schritt-Workflow

1. **Parteien extrahieren:** Verkaeufer, Kaeufer, Zielgesellschaft, Intermediar, Finanzier — volle Bezeichnung, Sitz, HR-Nummer
2. **Conflicts-Check ausfuehren:** § 43a BRAO; GwG-Screening (Sanktionen, PEP)
3. **Mandatsinformation erfassen:** Deal-Typ, Wert, Zeitplan, Vertraulichkeitsstufe, Partner-Zuordnung
4. **NDA-Status pruefen:** NDA unterzeichnet? Falls nicht: Einleitung vor weiterem Informationsaustausch
5. **Insiderinformations-Check:** boersennotiert → MAR-Insiderliste einleiten; Ad-hoc-Pruefung
6. **Deal-Karte erstellen:** Phase, Rolle, Owner, Frist, Risiko, naechste Aktion, Freigabegrad
7. **Aktenanlage und Mandatsvereinbarung:** Aktenzeichen vergeben; Honorarvereinbarung (§ 49b BRAO)

## Rote Schwellen

- Keine Conflicts-Pruefung vor Mandatsannahme: § 43a BRAO, Haftung
- GwG-Sorgfaltspflichten verletzt: Bussgeld
- Insiderinformation ohne MAR-Protokoll: aufsichtsrechtliche Konsequenzen
