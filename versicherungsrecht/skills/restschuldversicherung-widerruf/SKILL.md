---
name: restschuldversicherung-widerruf
description: "Restschuldversicherung Widerruf: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Restschuldversicherung Widerruf

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Restschuldversicherung Widerruf** im Plugin Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `restschuldversicherung-widerruf-kopplung-verbraucherdarlehen` | Restschuldversicherung bei Verbraucherdarlehen: Kopplung, Widerruf, Beratung, Kosten, Arbeitslosigkeit/Arbeitsunfähigkeit/Tod und Bankvertrieb prüfen. |
| `rueckversicherung-cut-through-und-fronting` | Rückversicherung, Fronting-Strukturen, Captives, Cut-through-Klauseln und Insolvenzrisiken rechtlich einordnen. |
| `solvency-ii-scr-orsa-aufsichtsrecht` | Solvency-II-Aufsichtsrahmen: Eigenmittel, SCR/MCR, ORSA, Governance, Ausgliederung und BaFin-Kommunikation für Versicherer und Gruppen. |

## Arbeitsweg

Im Plugin Versicherungsrecht gilt für **Restschuldversicherung Widerruf**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `restschuldversicherung-widerruf-kopplung-verbraucherdarlehen`

**Fokus:** Restschuldversicherung bei Verbraucherdarlehen: Kopplung, Widerruf, Beratung, Kosten, Arbeitslosigkeit/Arbeitsunfähigkeit/Tod und Bankvertrieb prüfen.

# Restschuldversicherung und Verbraucherdarlehen

## Einsatz

Für Verbraucher und Banken bei Streit um teure oder unpassende Restschuldversicherungen.

## Norm- und Quellenanker

VVG §§ 6, 7, 8; BGB Verbraucherdarlehen §§ 491 ff.; PAngV; IDD/Vermittlerrecht.

## Arbeitsfragen

1. Wie wurde die Versicherung mit dem Darlehen angeboten?
2. Wurden Kosten, Widerruf und Leistungsumfang transparent erklärt?
3. Welcher versicherte Fall ist eingetreten?
4. Ist Rückabwicklung, Leistung oder Beschwerde Ziel?

## Output

Kopplungsprüfung, Widerrufs-/Beratungsmemo, Leistungsantrag und Bankenbrief.

## Red Flags

- Versicherung im Effektivzins versteckt
- Gesundheits-/Arbeitslosigkeitsausschluss übersehen
- Widerrufsbelehrung lückenhaft
- Bank und Versicherer verweisen aufeinander

## Anschluss-Skills

- idd-vertrieb-beratung-dokumentation
- vag-bafin-aufsicht-beschwerde-missstand

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `rueckversicherung-cut-through-und-fronting`

**Fokus:** Rückversicherung, Fronting-Strukturen, Captives, Cut-through-Klauseln und Insolvenzrisiken rechtlich einordnen.

# Rückversicherung, Cut-through und Fronting

## Einsatz

Für Industrieprogramme, Captives und internationale Versicherungsstrukturen, in denen Erstversicherer und Rückversicherer auseinanderfallen.

## Norm- und Quellenanker

VVG/VAG Rückversicherung; BGB Vertragsauslegung; InsO; internationales Privatrecht.

## Arbeitsfragen

1. Wer ist Erstversicherer, Rückversicherer, Fronting Carrier, Captive?
2. Gibt es direkte Rechte des Versicherungsnehmers?
3. Welche Insolvenz- oder Sanktionsrisiken bestehen?

## Output

Strukturmemo, Anspruchslandkarte und Insolvenz-/Aufsichtsrisiko.

## Red Flags

- Cut-through nur behauptet
- Fronting Carrier insolvenzgefährdet
- anwendbares Recht fehlt

## Anschluss-Skills

- Nutze den allgemeinen Skill des Plugins, wenn Rolle, Police/Vertrag, Frist oder Ziel noch nicht klar sind.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `solvency-ii-scr-orsa-aufsichtsrecht`

**Fokus:** Solvency-II-Aufsichtsrahmen: Eigenmittel, SCR/MCR, ORSA, Governance, Ausgliederung und BaFin-Kommunikation für Versicherer und Gruppen.

# Solvency II, SCR und ORSA für Versicherer

## Einsatz

Für Rechtsabteilungen von Versicherern, Captives oder Investoren, die aufsichtsrechtliche Anforderungen verstehen und dokumentieren müssen.

## Norm- und Quellenanker

VAG; Delegierte Solvency-II-Regeln; EIOPA-Leitlinien; DORA bei IKT; HGB/IFRS nur als Schnittstelle.

## Arbeitsfragen

1. Welche Einheit: Versicherer, Rückversicherer, Gruppe, Vermittler, Ausgliederung?
2. Welche Kapital- und Governancepflicht ist betroffen?
3. Welche BaFin-/EIOPA-Vorgaben sind live zu prüfen?
4. Welche Dokumentation muss Vorstand/Aufsichtsrat sehen?

## Output

Aufsichtsmemo, ORSA-/Governance-Fragenliste, BaFin-Kommunikationsentwurf und Vorstandsvorlage.

## Red Flags

- SCR-Zahl ohne Governance-Kontext
- Ausgliederung nicht DORA-kompatibel
- Gruppe/Einzelunternehmen verwechselt
- Aufsichtsbrief zu langsam beantwortet

## Anschluss-Skills

- dora-cyber-ikt-versicherer
- eioPA-grenzueberschreitender-vertrieb

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
