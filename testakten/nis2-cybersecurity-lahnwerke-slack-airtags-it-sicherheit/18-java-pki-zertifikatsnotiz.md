# Java / PKI — Zertifikatsnotiz und Risikobewertung

## Tatsache

Das **Code-Signing-Zertifikat** für die Java-Build-Pipeline der Lahnwerke-Produktfirmware läuft am **09.07.2026** ab. Der Keystore mit dem privaten Schlüssel liegt nach Auskunft des Engineering-Teams aktuell **auf einem CI/CD-Runner-Volume** in einem Azure-DevOps-Pool, eingebunden als Persistent Volume (PV). Der **HSM-Einsatz** (Hardware Security Module) war im IT-Budget 2025 bereits eingeplant, wurde aber nie beauftragt — die Beschaffung scheiterte mehrfach an der Klärung der Verantwortlichkeit zwischen IT und Produktentwicklung. Der **Release 4.8** der Produktfirmware (geplant für 18.06.2026) hängt direkt am Zertifikat: Ohne gültige Signatur akzeptieren weder Engineering-Hosts noch Kundenanlagen die neue Firmware.

## Identifizierte Risiken

### 1. Ablaufrisiko Zertifikat (Compliance / Operations)

- Ohne rechtzeitige Erneuerung **wird Release 4.8 nicht ausgespielt werden können**.
- Bei Lieferverzug an Kunden mit vertraglich vereinbartem Release-Datum: Vertragsstrafenrisiko nach VOB-/Werk-/Liefervertragsklauseln; betroffen sind insbesondere die Kunden "Stahlring AG" (interner Konzernkunde) und "MARSEN GmbH" (Verzug-Pönale 5.000 EUR/Werktag).
- Bei nicht-signierten Notfall-Hotfixes: Eskalation in Kundeneinsatz.

### 2. Keystore-Lokalisierung (IT-Sicherheit)

- Der **Keystore auf einem Runner-Volume** widerspricht den allgemeinen Empfehlungen des BSI (BSI TR-03145) und der NIST SP 800-57. Korrekte Aufbewahrung wäre in einem HSM oder mindestens in einem dedizierten Vault mit Hardware-Bindung.
- Bei Kompromittierung des Runner-Volumes (etwa durch Diebstahl der CI-Pipeline-Credentials, kompromittierte Build-Skripte oder Insider-Zugriffe) wäre der private Schlüssel exfiltrierbar.
- Anschließende Schadenswirkung: Angreifer könnte beliebige Firmware signieren und in die Lahnwerke-Produktbasis einspeisen — **Lieferkettenangriff-Szenario** (z. B. SolarWinds-Typ).
- Diese Risikolage ist im Sinne der NIS2-Richtlinie (Art. 21 NIS2 iVm § 30 BSIG) ein "Cybersicherheitsrisiko, das angemessenes Risikomanagement erfordert" und unterliegt der Verantwortung der Geschäftsleitung.

### 3. Versäumte HSM-Beschaffung (Compliance Governance)

- HSM war 2025 budgetiert (intern Position "IT-Hardware 2025-IT-077"), wurde aber nie beschafft.
- Verantwortlich für die nicht-Beschaffung: ungeklärte Schnittstelle zwischen IT-Operations und Produktentwicklung; faktisch niemand.
- Geschäftsleitung muss **dokumentieren**, warum die Risikoreduzierungsmaßnahme nicht umgesetzt wurde, und welche kompensierenden Maßnahmen ergriffen wurden. Bei späterem Sicherheitsvorfall ist diese Dokumentation für die Frage der Geschäftsleiterhaftung (§ 91 Abs. 2 AktG; § 43 GmbHG) und Compliance-Pflicht entscheidend.

## Sofortmaßnahmen (heute)

### Operations (24-48 Stunden)

1. **Beschaffung eines Cloud-HSM** (z. B. Azure Key Vault Premium mit FIPS-140-2 Level 2 HSM, oder AWS CloudHSM) — schnellste Option, ohne Wartezeit auf physisches HSM.
2. **Schlüsselrotation**: Neuen Schlüssel im HSM erzeugen, neues Zertifikat bei der CA beantragen, alte Build-Pipeline auf neuen Schlüssel umstellen.
3. **Runner-Volume bereinigen**: privaten Schlüssel löschen, Audit-Log sichern.

### Compliance (1 Woche)

1. **Risikoregister-Eintrag**: aktuelles Risiko vollständig dokumentieren mit Schadenshöhe, Eintrittswahrscheinlichkeit, Mitigationsstatus.
2. **Geschäftsleitungs-Information**: Memo mit Risiko, Maßnahme, Restrisiko zur Kenntnisnahme.
3. **NIS2-Pflichtenprüfung**: Klären, ob das vorhandene Risiko ein "wesentlicher Sicherheitsvorfall" iSv § 32 BSIG (Umsetzung NIS2) wäre und ob Meldepflicht besteht. **Vorab**: derzeit kein Sicherheitsvorfall, sondern erkanntes Risiko — keine Meldepflicht; aber Dokumentationspflicht.

### Strategie (4 Wochen)

1. **Physisches HSM** beschaffen für langfristigen Einsatz (Nitrokey HSM oder Yubico YubiHSM; alternativ Thales nShield für Enterprise).
2. **Verantwortlichkeits-Matrix** zwischen IT-Ops und Produktentwicklung neu definieren — wer ist für CI/CD-Sicherheit ressortverantwortlich.
3. **Audit der gesamten CI/CD-Pipeline**: weitere Geheimnisse (Secrets, Tokens, Zertifikate) lokalisieren und in den Vault verlagern.

## NIS2-Relevanz

- **Art. 21 NIS2** (Maßnahmen für Cybersecurity-Risikomanagement): Kryptografie, Zugangskontrolle, Lieferkettenschutz sind Pflichtmaßnahmen.
- **Geschäftsleitungs-Pflichten** Art. 20 NIS2 (in deutscher Umsetzung § 35 BSIG): Geschäftsleitung muss "die getroffenen Maßnahmen genehmigen, deren Umsetzung beaufsichtigen und kann persönlich haftbar werden, wenn sie ihre Pflichten verletzt".
- Bei einem späteren Vorfall, der auf den hier dokumentierten Mangel zurückgeht, wäre die Frage zu beantworten: warum wurde das Risiko nicht behoben?

## Verantwortlichkeiten

- **CISO**: heute Risikoregister aktualisieren, Cloud-HSM-Beschaffung anstoßen.
- **IT-Operations**: Schlüsselrotation operationell vorbereiten.
- **Geschäftsleitung**: Memo bis 06.06.2026 zur Kenntnisnahme; Freigabe Beschaffung.
- **Externe Beratung**: Spezialfrage Schlüsselverwaltung in CI/CD-Pipelines an Beratung Klein+Steinberg (vorgesehen).
