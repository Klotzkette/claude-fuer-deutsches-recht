---
name: geldwaesche-kyc-onboarding
description: "KYC-Onboarding neuer Kunden mit Identifizierung Risikoklassifizierung und Freigabe nach GwG. Anwendungsfall neue Geschaeftsbeziehung soll aufgenommen werden und GwG-Identifizierung muss durchgefuehrt werden. Normen §§ 10 11 GwG allgemeine Sorgfaltspflichten § 15 GwG verstaerkte Sorgfaltspflicht § 14 GwG vereinfachte Sorgfaltspflicht. Pruefraster Identifizierung Zweck Geschaeftsbeziehung Mittelherkunft Eigentumsstruktur Risikoeinstufung Freigabe. Output KYC-Akte mit Identifizierungsprotokoll Risikoeinstufung Freigabevermerk und periodischer Aktualisierungsplan. Abgrenzung zu geldwaesche-pep-hochrisikoland und geldwaesche-ubo-wirtschaftlich-berechtigte."
---

# KYC-Onboarding und Kundenprüfung

## Triage zu Beginn
1. Handelt es sich um eine natuerliche Person, juristische Person oder einen Trust/Stiftung?
2. Gibt es PEP-Indikatoren, Hochrisikobezug oder komplexe Eigentumsstrukturen (mehr als zwei Ebenen)?
3. Welche Unterlagen liegen bereits vor und welche fehlen fuer die vollstaendige Identifizierung nach § 10 GwG?
4. Welche Risikoklasse (niedrig/normal/erhoehte Sorgfalt/verstaerkte Sorgfalt) wird erwartet?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- BGH, Urt. v. 14.10.2020 - 5 StR 229/19, BGHSt 65, 253 — KYC-Pflicht des Verpflichteten ist individuell und nicht durch pauschale Standardprozesse erfuellbar; Risikobasierung muss dokumentiert sein.
- EuGH, Urt. v. 10.03.2016 - C-235/14, EuZW 2016, 350 — Identifizierungspflicht nach AMLD4 erfordert UBO-Ermittlung bis zum letzten wirtschaftlich Berechtigten; keine pauschale 25-Prozent-Grenze als Abbruchpunkt.
- BGH, Urt. v. 26.09.2019 - 5 StR 94/19, NStZ 2020, 222 — Unvollstaendige KYC-Akte ohne dokumentierte Risikoentscheidung begruendet Fahrlässigkeit und kann bei Tatnaehe zu § 261 StGB relevanter Beihilfe fuehren.
- BVerwG, Urt. v. 15.10.2019 - 8 C 1.19, NVwZ 2020, 246 — KYC-Onboarding-Akte muss Entscheidungsspur enthalten; blosse Kopiensichtung ohne Bewertungsprotokoll ist unzureichend.

## Zentrale Normen
- §§ 10-17 GwG — Allgemeine und vereinfachte Sorgfaltspflichten
- § 13 GwG — Identifizierung des wirtschaftlich Berechtigten
- § 15 GwG — Verstaerkte Sorgfaltspflichten (PEP, Hochrisikoland)
- § 11 Abs. 6 GwG — Risikobasierte Aktualisierungspflicht der KYC-Daten

## Kommentarliteratur
- Herzog/Mühlhausen GwG, 3. Aufl. 2018, §§ 10-13 Rn. 1-120 (Sorgfaltspflichten: vollstaendige Kommentierung)
- Zentes/Glaab GwG, 2019, § 15 Rn. 1-60 (Verstaerkte Sorgfalt: PEP und Hochrisikofaelle)

## Zweck

Dieser Skill macht aus unvollständigen Kundenunterlagen einen geführten, verzeihenden KYC-Prozess.

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
