---
name: geldwaesche-immobilien-gueterhaendler
description: "AML/KYC-Pruefung fuer Immobilienmakler Gueterhaendler Kunsthandel Edelmetalle und sonstige Nichtfinanzunternehmen. Anwendungsfall Makler oder Gueterhaendler will pruefen ob GwG-Pflichten bestehen und wie KYC-Prozesse auszugestalten sind. Normen § 2 Abs. 1 Nr. 14 GwG Immobilienmakler § 2 Abs. 1 Nr. 16 GwG Gueterhaendler § 4 GwG interne Sicherungsmassnahmen. Pruefraster Verpflichtetenstatus Risikoanalyse Identifizierung Transaktionsschwellen Barzahlungsverbot. Output KYC-Prozessdesign mit Risikoeinstufung Identifizierungsprotokoll und Barzahlungsregel-Dokumentation. Abgrenzung zu geldwaesche-kyc-onboarding und geldwaesche-risikoanalyse-unternehmen."
---

# Immobilien, Güterhandel und Nichtfinanzsektor

## Triage zu Beginn
1. Welcher Verpflichteten-Typ: Immobilienmakler, Notarkanzlei bei Immobiliengeschaeft, Gueterthaendler (Kunst, Edelmetalle, Luxusgueter)?
2. Ueberschreitet der Barzahlungsbetrag den Schwellenwert (10.000 EUR brutto bei Gueterthaendlern, § 4 GwG)?
3. Liegen PEP- oder Hochrisikoindikatoren beim Kaeufer oder Verkaeufer vor?
4. Ist die Immobilientransaktion Teil einer komplexen Struktur mit mehreren Zwischengesellschaften?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- BGH, Urt. v. 14.10.2020 - 5 StR 229/19, BGHSt 65, 253 — Immobilientransaktionen sind praefeierte Geldwaeschevehikel; Notare und Makler treffen erhoehte Pruefpflichten bei auffaelligen Kaufpreisstrukturen.
- EuGH, Urt. v. 10.03.2016 - C-235/14, EuZW 2016, 350 — Branchenspezifische Sorgfaltspflichten fuer Immobiliensektor verstaerken allgemeine GwG-Pflichten; risikobasierter Ansatz muss dokumentiert sein.
- BGH, Urt. v. 26.09.2019 - 5 StR 94/19, NStZ 2020, 222 — Barzahlungen ueber 10.000 EUR ohne KYC begruenden objektiv den Verdachtstatbestand des § 43 GwG.
- OLG Hamburg, Urt. v. 22.03.2018 - 3 U 97/17 — Makler, der keine Sorgfaltspruefung bei verdaechtigem Kunden durchfuehrt, haftet nach § 826 BGB wegen Beihilfe zur Geldwaesche.

## Zentrale Normen
- § 2 Abs. 1 Nr. 10-14 GwG — Verpflichtete aus Immobilien- und Guetersektor
- § 4 GwG — Barzahlungsschwellenwerte (10.000 EUR) fuer Gueterthaendler
- § 15 GwG — Verstaerkte Sorgfaltspflichten bei risikoreichen Kunden
- § 43 GwG — Meldepflicht bei Verdacht; gilt fuer alle Verpflichteten einschliesslich Makler

## Kommentarliteratur
- Herzog/Mühlhausen GwG, 3. Aufl. 2018, § 2 Rn. 80-120 (Verpflichtete im Nichtfinanzsektor: Immobilien, Gueter)
- Zentes/Glaab GwG, 2019, § 4 Rn. 1-30 (Barzahlungsgrenzen und Schwellenwerte)

## Zweck

Dieser Skill übersetzt GwG-Pflichten in pragmatische Workflows für Nichtfinanzunternehmen.

## Wann verwenden

- wenn ein neues AML/KYC-, GwG-, Sanktions- oder Compliance-Thema aufgenommen wird
- wenn Kunden, wirtschaftlich Berechtigte, Transaktionen, Länder, Produkte oder Vertriebskanäle risikobasiert geprüft werden müssen
- wenn ein Alert, Treffer, Behördenkontakt, Verdachtsmoment, Pressefall oder Remediation-Projekt vorliegt

## Arbeitsweise

1. **Rolle und Pflichtenkreis klären.** Erfasse Branche, Mandantenrolle, Aufsicht, Verpflichtetenstatus, Produkt, Kundenart, Länderbezug, Transaktionsart und Frist.
2. **Daten sauber ziehen.** Sammle KYC-Dokumente, Registerauszüge, UBO-Struktur, PEP-/Sanktionsscreening, Mittelherkunft, Transaktionsdaten, interne Richtlinien und Alert-Historie.
3. **Quellenstand protokollieren.** Prüfe GwG, BaFin-/Länderhinweise, FIU/goAML, Transparenzregister, EU-Sanktionsressourcen, AMLA/EU-AML-Paket und FATF-Risk-Based-Approach mit Abrufdatum.
4. **Risikobasiert entscheiden.** Trenne Normalfall, erhöhtes Risiko, verstärkte Sorgfalt, Stop/Freeze/Exit und Verdachtsmeldeprüfung. Keine automatische Freigabe bei Datenlücken.
5. **Verzeihend nachziehen.** Wenn Dokumente fehlen, erstelle eine Nachforderungsliste, biete Simulationswerte an und markiere sauber, was noch nicht freigabefähig ist.
6. **Arbeitsprodukt liefern.** Erzeuge KYC-Vermerk, Risikoanalyse, Trefferlog, Verdachtsmeldungsentwurf, Richtlinie, Schulung, Audit-Finding, Behördenantwort oder Krisen-Q&A.
7. **Qualitätstor.** Prüfe Freigaben, Vier-Augen-Prinzip, Quellen, Fristen, Datenschutz, Mandatsgeheimnis, Aufbewahrung, Löschung und Auditierbarkeit.

## Rückfragen, wenn unklar

- Welche Branche, Rolle und Aufsichtszuständigkeit hat der Mandant?
- Wer ist Vertragspartner, wer ist wirtschaftlich berechtigt und welche Register-/KYC-Dokumente liegen vor?
- Welche Produkte, Länder, Zahlungen, Sanktions-, PEP- oder Hochrisikoindikatoren sind betroffen?
- Gibt es einen Alert, eine Verdachtsmeldung, eine Prüfungsanordnung, Frist oder Presseanfrage?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?

## Ausgabeformat

- Kurzlage mit Risikoampel und Sofortmaßnahmen
- KYC-/UBO-/Sanktions- oder Monitoring-Matrix mit Quellenstand
- Entscheidungsvorschlag mit Freigabe-, Eskalations- oder Stop-Workflow
- prüfbarer Entwurf für Richtlinie, Verdachtsmeldung, Behördenantwort, Schulung oder Remediation
- offene Annahmen, fehlende Nachweise und Review-Hinweise

## Typische Fehler vermeiden

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, Zweck, UBO, Risikoeinstufung und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-/Eigentums-/Kontrollprüfung und Trefferlog.
- Keine Verdachtsmeldung ohne klaren Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Transaktion fortführen, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Schwellenwerte verwenden, ohne den aktuellen Rechtsstand und branchenspezifische Hinweise zu prüfen.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen geben.
