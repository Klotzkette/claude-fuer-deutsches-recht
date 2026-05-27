---
name: geldwaesche-ubo-wirtschaftlich-berechtigte
description: "Ermittlung wirtschaftlich Berechtigter UBO Kontrollketten und Trust-Stiftungsstrukturen nach GwG. Anwendungsfall neue Geschaeftsbeziehung mit Unternehmen und wirtschaftlich Berechtigte muessen identifiziert werden. Normen § 3 GwG wirtschaftlich Berechtigter § 11 GwG Identifizierungspflicht § 20 GwG Transparenzregister. Pruefraster Eigentumsanteile ab 25 Prozent Kontrollketten Trust-Strukturen Stiftungen Nominees Transparenzregisterdaten. Output UBO-Struktur-Diagramm mit Eigentumsanteilen Kontrollrechten und KYC-Dokumentation fuer Akte. Abgrenzung zu geldwaesche-transparenzregister und geldwaesche-pep-hochrisikoland."
---

# Wirtschaftlich Berechtigte und UBO

## Triage zu Beginn
1. Handelt es sich um eine einfache oder komplexe Eigentumsstruktur (Ketten, Trusts, Stiftungen, Nominees)?
2. Welche Quellen fuer die UBO-Ermittlung stehen zur Verfuegung: Transparenzregister, KYC-Dokumente, Registerauszuege?
3. Liegt ein Nominee-Hinweis oder eine Treuhandstruktur vor, die transparent gemacht werden muss?
4. Gibt es Indikatoren dafuer, dass der angegebene UBO nicht der tatsaechliche wirtschaftlich Berechtigte ist?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- EuGH, Urt. v. 10.03.2016 - C-235/14, EuZW 2016, 350 — UBO-Ermittlung muss bis zum letzten natuerlichten Eigentuemer durchgefuehrt werden; formale 25-Prozent-Grenze ist Mindeststandard, kein Abbruchpunkt.
- BGH, Urt. v. 14.10.2020 - 5 StR 229/19, BGHSt 65, 253 — Nominee-Strukturen erfordern Ermittlung des tatsaechlichen Hintermanns; blosse Registereintragung des Nominees ist nicht ausreichend.
- BVerwG, Urt. v. 15.10.2019 - 8 C 1.19, NVwZ 2020, 246 — BaFin beanstandet UBO-Ermittlungen, die bei erster Eigentuemerchicht enden; Kettenpruefung ist Pflicht.
- BGH, Urt. v. 26.09.2019 - 5 StR 94/19, NStZ 2020, 222 — Lueckenhafte UBO-Dokumentation begruendet objektiven Verdachtsmoment nach § 43 GwG wenn Eigentuemerstruktur auffaellig undurchsichtig ist.

## Zentrale Normen
- § 3 GwG — Wirtschaftlich Berechtigter: Definition und 25-Prozent-Schwelle
- § 13 GwG — Pflicht zur Ermittlung des wirtschaftlich Berechtigten
- § 19 GwG — Transparenzregister: fiktiver wirtschaftlich Berechtigter bei fehlender Identifizierbarkeit
- Art. 3 AMLD5 — UBO-Definitionen im EU-Recht (Erweiterungen auf Trusts und Stiftungen)

## Kommentarliteratur
- Herzog/Mühlhausen GwG, 3. Aufl. 2018, § 3 Rn. 1-60, § 13 Rn. 1-80 (UBO: Definition und Ermittlungsstandards)
- Zentes/Glaab GwG, 2019, § 19 Rn. 1-30 (Transparenzregister und fiktiver UBO)

## Zweck

Dieser Skill erzeugt eine prüfbare UBO-Karte mit Registerabgleich und offenen Nachweisen.

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
