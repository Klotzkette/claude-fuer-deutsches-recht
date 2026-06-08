---
name: onboarding-mandantenkommunikation
description: "Leitfaden zur Mandantenkommunikation in steuerlichen Mandaten — wann muss aufgeklaert werden wie wird dokumentiert und welche Fallstricke schaffen Haftungsrisiko für Anwalt und Steuerberater. Anwendungsfall Berater hat eine Empfehlung zu unterbreiten die Mehrsteuer Nachzahlungszinsen oder strafrechtliche Risiken aufwirft und muss dies dokumentieren. Behandelt Hinweispflicht auf Risiken Steuergefahren Vorteilhaftigkeitsvergleich Aufklaerung ueber Vergleichswege und Dokumentation in der Akte. Output Aufklaerungsbogen und Bestaetigungsmuster. Abgrenzung zu fa-stu-onboarding-mandatsannahme und fa-stu-rvg-steuerstreit."
---

# Mandantenkommunikation und Aufklaerungspflicht im Steuerrecht

## Fachlicher Anker

- **Normen:** § 6a, § 371 AO, § 153 AO.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Triage — kläre vor der Bearbeitung

1. Welche Handlungsalternativen bestehen und welche Mehr- oder Minder-Steuer ist mit jeder verbunden?
2. Welches Steuerstrafrisiko ist erkennbar — muss zwingend auf § 371 AO und § 153 AO hingewiesen werden?
3. Welche Fristen laufen — hat der Mandant verstanden dass Untaetigkeit zur Bestandskraft fuehrt?
4. Wurde der Mandant ueber Honorarrahmen und Kostenrisiken aufgeklaert?
5. Wurde die Empfehlung schriftlich oder mit Aktenvermerk dokumentiert?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

- **§ 280 BGB** — Schadensersatz wegen Pflichtverletzung; Anwalts- und Steuerberaterhaftung.
- **§ 675 BGB** — entgeltliche Geschaeftsbesorgung.
- **§ 33 StBerG** — Berufsbild Steuerberater; eigenverantwortliche Vertretung.
- **§ 43a Abs. 3 BRAO** — Sachlichkeitsgebot; Beratung sachlich und vollstaendig.
- **§ 153 AO** — Berichtigungspflicht bei nachtraeglich erkannter Unrichtigkeit.
- **§ 371 AO** — Selbstanzeige.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesfinanzhof.de, bundesverfassungsgericht.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Pauschalzitate aus BeckRS allein; jede Entscheidung muss auf eine primaere oder offene Sekundaerquelle ruckfuehrbar sein.

## Zentrale Normen

§ 280 BGB · § 675 BGB · § 33 StBerG · § 43a BRAO · § 153 AO · § 371 AO · § 89 AO (verbindliche Auskunft) · § 204 AO (verbindliche Zusage)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Verwaltungsanweisungen (BMF-Schreiben, OFD-Verfuegungen, AEAO, UStAE, EStR, KStR) ausschliesslich nach Verifikation aus bundesfinanzministerium.de oder offiziellen Amtsblaettern zitieren.

## Praxisformulierung / Antragsmuster

```
AUFKLAERUNGS- UND ENTSCHEIDUNGSBESTAETIGUNG

Mandant: [NAME], [ADRESSE]
Berater: [NAME], [KANZLEI]
Sache: [STEUERART, JAHR, AKTENZEICHEN]

Heute am [DATUM] habe ich folgende Handlungsoptionen erlaeutert:
1. [OPTION A] — voraussichtliche Mehrsteuer: [BETRAG]; Risiken: [...]
2. [OPTION B] — voraussichtliche Mehrsteuer: [BETRAG]; Risiken: [...]
3. Untaetigkeit — Folge: Bestandskraft des Bescheids.

Ausdruecklich hingewiesen wurde auf:
- Berichtigungspflicht nach § 153 AO bei nachtraeglichem Erkennen einer Unrichtigkeit
- Moeglichkeit der Selbstanzeige nach § 371 AO und ihre Sperrgruende
- Nachzahlungszinsen § 233a AO und Hinterziehungszinsen § 235 AO
- Frist und Kosten

Der Mandant entscheidet sich für Option [...].

[ORT, DATUM] [UNTERSCHRIFT MANDANT] [UNTERSCHRIFT BERATER]
```

## Abgrenzung zu anderen Skills dieses Plugins

- Verfahrens-Sklls (`anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-akteneinsicht-steuerakte`) decken den prozessualen Rahmen ab; dieser Skill liefert die **materielle** Begruendung.
- Bei steuerstrafrechtlichen Beruehrungspunkten parallel `fa-stu-steuerhinterziehung-370-ao` und `fa-stu-selbstanzeige-371-ao` aufrufen.
- Bei berufsrechtlichen Fragestellungen `fa-stu-stberg-vereinbare-taetigkeit` bzw. `fa-stu-rvg-steuerstreit` parallel ziehen.
