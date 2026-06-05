---
name: anzeige-beweismatrix-chatverlaeufe
description: "Anzeige Beweismatrix Chatverlaeufe: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anzeige Beweismatrix Chatverlaeufe

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Anzeige Beweismatrix Chatverlaeufe** im Plugin Strafanzeige Vorbereiter. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anzeige-beweismatrix-tatsachen-meinungen` | Ordnet jedes Element der Anzeige nach Tatsachenwissen, Beleg, Zeuge, Dokument, Meinung und Vermutung. |
| `anzeige-chatverlaeufe-emails-header` | Chatverläufe, EML-Dateien, E-Mail-Header, Messenger-Screenshots, Export und Kontext sichern. |

## Arbeitsweg

Im Plugin Strafanzeige Vorbereiter gilt für **Anzeige Beweismatrix Chatverlaeufe**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anzeige-beweismatrix-tatsachen-meinungen`

**Fokus:** Ordnet jedes Element der Anzeige nach Tatsachenwissen, Beleg, Zeuge, Dokument, Meinung und Vermutung.

# Beweismatrix: Tatsache, Meinung, Vermutung

## Einsatz

Für saubere Anzeigen ohne Überbehauptung.

## Norm- und Quellenanker

StPO § 158; StGB § 164; ZPO Beweisgrundsätze.

## Arbeitsfragen

1. Welche Aussage ist Tatsache?
2. Welcher Beleg?
3. Welche Vermutung muss als solche markiert werden?

## Output

Beweismatrix und Anlagenliste.

## Red Flags

- Adjektive ersetzen Beweise
- Screenshots ohne Kontext
- Zeuge unklar

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `anzeige-chatverlaeufe-emails-header`

**Fokus:** Chatverläufe, EML-Dateien, E-Mail-Header, Messenger-Screenshots, Export und Kontext sichern.

# Chats, E-Mails und Header sichern

## Einsatz

Für digitale Kommunikation als Hauptbeweis.

## Norm- und Quellenanker

StPO; ZPO; DSGVO; Fernmeldegeheimnis je Kontext.

## Arbeitsfragen

1. Welcher Kommunikationskanal?
2. Sind vollständige Verläufe vorhanden?
3. Wer ist Absender?

## Output

Kommunikationsbeweis-Paket.

## Red Flags

- einzelne Chatfetzen
- Header fehlen
- Weiterleitung verändert Beweis

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
