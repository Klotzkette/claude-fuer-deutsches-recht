---
name: zugang-kuendigung-mehrfachzustellung
description: "Zugang Kuendigung Mehrfachzustellung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Zugang Kuendigung Mehrfachzustellung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Zugang Kuendigung Mehrfachzustellung** im Plugin Arbeitsrecht (BGB §§ 611a ff., KSchG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zugang-neu-006-kuendigung-per-bea-e-mail-fax-und-schriftformfall` | Arbeitsrecht: Kündigung per beA E-Mail Fax und Schriftformfallen mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis. |
| `zugang-neu-007-mehrfachzustellung-kuendigung-sicherheitskonzept` | Arbeitsrecht: Mehrfachzustellung Kündigung Sicherheitskonzept mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis. |

## Arbeitsweg

Im Plugin Arbeitsrecht (BGB §§ 611a ff., KSchG) gilt für **Zugang Kuendigung Mehrfachzustellung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zugang-neu-006-kuendigung-per-bea-e-mail-fax-und-schriftformfall`

**Fokus:** Arbeitsrecht: Kündigung per beA E-Mail Fax und Schriftformfallen mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis.

# Zugang Kuendigung Per Bea E Mail Fax Und Schriftformfall

## Aufgabe

Skill fuer Kuendigung per beA / E-Mail / Fax — und der Schriftformfalle § 623 BGB.

## Schriftformerfordernis § 623 BGB

- **Kuendigung erfordert SCHRIFTFORM** (= eigenhaendige Unterschrift im Original, § 126 BGB).
- Elektronische Form (§ 126a BGB qualifizierte elektronische Signatur) ist NUR ausnahmsweise gleichgestellt — und im Arbeitsrecht durch § 623 BGB AUSGESCHLOSSEN.

## Was funktioniert NICHT

- Einfache E-Mail (auch mit eingescannter Unterschrift).
- Fax (BAG 6 AZR 519/12).
- WhatsApp/SMS.
- beA-Nachricht (qualifizierte Signatur reicht nach § 623 BGB nicht).

## Folge

- Nicht-schriftliche Kuendigung ist **nichtig** § 125 BGB.
- Keine Wirkung — Arbeitsverhaeltnis besteht fort.
- **§ 4 S. 1 KSchG laeuft NICHT an**, weil die Vorschrift ihrem Wortlaut nach nur eine **schriftliche** Kuendigung erfasst (BAG 22. Oktober 2015 - 2 AZR 720/14 Rn 23 ff.; BAG 17. Dezember 2015 - 6 AZR 709/14).
- **Keine Heilung ueber § 7 KSchG** bei Formverstoss: Die Fiktionswirkung des § 7 KSchG setzt eine formwirksame schriftliche Kuendigung voraus; bei Nichtigkeit nach § 125 BGB iVm § 623 BGB greift sie nicht.
- Der Arbeitnehmer kann den Fortbestand des Arbeitsverhaeltnisses jederzeit (vorbehaltlich Verwirkung) mit allgemeiner Feststellungsklage § 256 ZPO geltend machen, nicht nur mit Kuendigungsschutzklage § 4 KSchG.
- Achtung Abgrenzung: Eine formwirksame, aber aus anderem Grund unwirksame Kuendigung (z.B. Sozialwidrigkeit, fehlende Anhoerung Betriebsrat) muss innerhalb von 3 Wochen mit Kuendigungsschutzklage angegriffen werden, sonst Fiktion § 7 KSchG.

## Empfehlung

- **Original-Brief mit eigenhaendiger Unterschrift** ist der einzig sichere Weg.
- Zustellung per Bote oder persoenliche Uebergabe.
- Wenn elektronisch, dann nur als Vorab-Information; Original folgt.

## BAG-Linie

- BAG 6 AZR 519/12: Fax-Kuendigung formnichtig.
- BAG 6 AZR 687/09: keine E-Mail-Kuendigung.
- BAG 2 AZR 224/18: Zugangsfragen.

## Pruefraster

1. Welches Medium?
2. Schriftform eingehalten?
3. Wenn nein: Nichtigkeit + Klage?
4. 3-Wochen-Frist beachten?

## Output

- Form-Analyse.
- Klageempfehlung bei Formverstoss.

## 2. `zugang-neu-007-mehrfachzustellung-kuendigung-sicherheitskonzept`

**Fokus:** Arbeitsrecht: Mehrfachzustellung Kündigung Sicherheitskonzept mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis.

# Zugang Mehrfachzustellung Kuendigung Sicherheitskonzept

## Aufgabe

Skill fuer Mehrfachzustellung der Kuendigung als Sicherheitskonzept gegen Beweisschwierigkeiten.

## Hintergrund

Wegen der hohen Beweislast (Arbeitgeber muss Zugang beweisen) und der 3-Wochen-Frist § 4 KSchG ist Mehrfachzustellung Best Practice.

## Empfohlene Kombinationen

### Kombi 1: Bote + Einwurfeinschreiben
- Bote uebergibt persoenlich (Erstzugang).
- Einwurfeinschreiben am gleichen Tag oder kurz danach (Ersatzbeweis).

### Kombi 2: Persoenliche Uebergabe + Einschreiben mit Rueckschein
- Persoenliche Uebergabe gegen Empfangsbestaetigung.
- Einschreiben mit Rueckschein zusaetzlich (falls Empfangsbestaetigung verloren).

### Kombi 3: Bote + Notar
- Notar zustellt nach §§ 132-135 ZPO analog.
- Beste Beweisqualitaet (oeffentliche Urkunde).

## Risiko der Mehrfachzustellung

- Mehrere Zugangszeitpunkte: massgeblich ist der FRUEHSTE wirksame Zugang.
- Folge fuer Klagefrist: laeuft ab dem fruehsten Zugang.

## Praxistipps

- Datum, Uhrzeit jeder Zustellung protokollieren.
- Identische Originale (Inhaltsbeweis).
- Bei Streit ueber Zugang: spaetestens Zustellung wirkt.

## Pruefraster

1. Wie viele Zustellwege?
2. Welcher war zuerst wirksam?
3. Beweismittel pro Weg?

## Output

- Zustellplan mit Multipfad.
- Beweissicherung-Matrix.
