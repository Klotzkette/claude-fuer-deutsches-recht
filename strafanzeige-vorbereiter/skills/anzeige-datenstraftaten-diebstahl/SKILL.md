---
name: anzeige-datenstraftaten-diebstahl
description: "Anzeige Datenstraftaten Diebstahl: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anzeige Datenstraftaten Diebstahl

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Anzeige Datenstraftaten Diebstahl** im Plugin Strafanzeige Vorbereiter. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anzeige-datenstraftaten-202a-303a` | Ausspähen, Abfangen, Datenveränderung, Computersabotage: technische Beweise, Logs, Forensik und ZAC. |
| `anzeige-diebstahl-unterschlagung` | Diebstahl/Unterschlagung anzeigen: Gewahrsam, Eigentum, Wegnahme, Zueignung, Beweise, Herausgabeverlangen. |

## Arbeitsweg

Im Plugin Strafanzeige Vorbereiter gilt für **Anzeige Datenstraftaten Diebstahl**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anzeige-datenstraftaten-202a-303a`

**Fokus:** Ausspähen, Abfangen, Datenveränderung, Computersabotage: technische Beweise, Logs, Forensik und ZAC.

# Datenstraftaten §§ 202a, 303a StGB

## Einsatz

Für Hacking, Accountübernahme, Datenlöschung.

## Norm- und Quellenanker

StGB §§ 202a–202d, 303a, 303b; DSGVO Art. 33.

## Arbeitsfragen

1. Welche Systeme/Daten?
2. Welche Logs/Forensik?
3. Welche parallelen Meldepflichten?

## Output

Datenstraftaten-Anzeige und Incident-Check.

## Red Flags

- Systeme verändert
- Passwörter nicht gesperrt
- DSGVO-Meldung vergessen

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `anzeige-diebstahl-unterschlagung`

**Fokus:** Diebstahl/Unterschlagung anzeigen: Gewahrsam, Eigentum, Wegnahme, Zueignung, Beweise, Herausgabeverlangen.

# Diebstahl und Unterschlagung

## Einsatz

Für Sachen, Geräte, Waren, Firmenlaptops.

## Norm- und Quellenanker

StGB §§ 242, 246; BGB Eigentum/Besitz.

## Arbeitsfragen

1. Wem gehört was?
2. Wer hatte Gewahrsam?
3. Welche Beweise?

## Output

Anzeige mit Eigentums-/Besitzmatrix.

## Red Flags

- Vertragsrückgabe als Diebstahl
- Eigentum unklar
- Inventarliste fehlt

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
