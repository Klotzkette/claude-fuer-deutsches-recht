---
name: anzeige-datenstraftaten-diebstahl
description: "Anzeige Datenstraftaten 202a 303a, Anzeige Diebstahl Unterschlagung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Anzeige Datenstraftaten 202A 303A, Anzeige Diebstahl Unterschlagung

## Arbeitsbereich

Dieser Skill bündelt **Anzeige Datenstraftaten 202A 303A, Anzeige Diebstahl Unterschlagung** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `anzeige-datenstraftaten-202a-303a` | Ausspähen, Abfangen, Datenveränderung, Computersabotage: technische Beweise, Logs, Forensik und ZAC. |
| `anzeige-diebstahl-unterschlagung` | Diebstahl/Unterschlagung anzeigen: Gewahrsam, Eigentum, Wegnahme, Zueignung, Beweise, Herausgabeverlangen. |

## Arbeitsweg

Für **Anzeige Datenstraftaten 202A 303A, Anzeige Diebstahl Unterschlagung** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `strafanzeige-vorbereiter` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

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
