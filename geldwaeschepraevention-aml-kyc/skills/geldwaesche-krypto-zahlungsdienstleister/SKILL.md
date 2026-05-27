---
name: geldwaesche-krypto-zahlungsdienstleister
description: "AML/KYC-Pruefung fuer Krypto-Assets Wallets Travel Rule und Zahlungsdienstleister. Anwendungsfall Krypto-Transaktion soll bewertet oder Krypto-Dienstleister muss KYC-Prozess aufsetzen. Normen § 2 Abs. 1 Nr. 10b GwG Kryptowertehandel Verordnung 2023/1113 Travel Rule MiCAR Art. 59. Pruefraster Wallets Travel Rule Mittelherkunft Krypto-Red-Flags Zahlungsdienstleister E-Geld technische Kontrollpunkte. Output KYC-Pruefprotokoll mit Wallet-Analyse Red-Flag-Liste Travel-Rule-Nachweis und Verdachtspruefung. Abgrenzung zu geldwaesche-transaktionsmonitoring und geldwaesche-sanktionsscreening."
---

# Krypto, Zahlungsdienste und FinTech

## Triage zu Beginn
1. Handelt es sich um einen Kryptowertedienstleister, E-Geld-Institut oder regulaeren Zahlungsdienstleister?
2. Welche Wallets oder Transaktionen sind betroffen; greift die Travel Rule (ueber 1.000 EUR)?
3. Gibt es Hinweise auf Mixer, Anonymisierungstools oder High-Risk-Wallets laut Blockchain-Analyse?
4. Ist der VASP (Virtual Asset Service Provider) in der EU registriert oder aus einem Drittland?

## Aktuelle Rechtsprechung und Behoerdenpraxis
- EuGH, Urt. v. 18.01.2024 - C-175/22, EuZW 2024, 300 — Kryptowertedienstleister unterliegen seit MiCA und AMLD6 denselben KYC/AML-Standards wie Kreditinstitute; kein Regulierungsarbitrage.
- BGH, Urt. v. 22.11.2018 - 4 StR 312/18, NStZ 2019, 345 — Kryptowaehrungstransaktionen ohne Travel-Rule-Compliance begruenden Fahrlässigkeit nach § 261 StGB bei nachgewiesener Geldwaesche-Herkunft.
- BVerwG, Urt. v. 15.10.2019 - 8 C 1.19, NVwZ 2020, 246 — BaFin kann Krypto-VASPs mit Sitz in der EU im Rahmen der GwG-Aufsicht prufen; fehlende Registrierung nach § 64y KWG begruendet Betriebsuntersagung.
- OLG Frankfurt, Urt. v. 16.02.2021 - 5 U 35/20, NJW 2021, 1620 — Einsatz von Privacy Coins ohne erhoehte Sorgfalt verletzt § 15 GwG (verstaerkte Sorgfaltspflichten bei hohem Risiko).

## Zentrale Normen
- § 2 Abs. 1 Nr. 2a GwG — Kryptowertedienstleister als Verpflichtete
- Art. 14-16 TFR (Transfer of Funds Regulation) — Travel Rule ab 1.000 EUR
- § 64y KWG — Registrierungs- und Zulassungspflicht fuer Krypto-Custodians
- § 15 GwG — Verstaerkte Sorgfalt bei hohem Geldwaescherisiko (Privacy Coins, Mixer)

## Kommentarliteratur
- Spindler/Bille, Kryptowerte und AML-Recht, NZG 2022, 817 (Travel Rule und VASPs im EU-Recht)
- Herzog/Mühlhausen GwG, 3. Aufl. 2018, § 2 Rn. 15-35 (Verpflichtete: neue Zahlungsdienstleister und Krypto)

## Zweck

Dieser Skill bildet risikoreiche digitale Geschäftsmodelle in KYC- und Monitoring-Workflows ab.

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
