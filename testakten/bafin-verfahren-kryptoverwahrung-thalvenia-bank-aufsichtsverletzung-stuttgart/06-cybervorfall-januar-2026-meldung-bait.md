# 06 — Cybervorfall Januar 2026 und BAIT-Meldung

**Vorfallsdatum:** 9. Januar 2026, 02:17 Uhr (Erstalarm im SIEM-System)
**Intern klassifiziert:** IT-Notfall Stufe 2 (von 3)
**Erstmeldung an BaFin:** 13. Januar 2026, 14:32 Uhr
**Meldungsverzug:** rd. 96 Stunden (4 Tage)

---

## Technischer Sachverhalt

In der Nacht vom 8. auf den 9. Januar 2026 infiltrierten unbekannte Angreifer das Netzwerk der Thalvenia Bank AG über eine ungepatchte Schwachstelle im VPN-Gateway (Fortinet FortiGate, CVE-2024-21762). Die Angreifer erlangten zunächst Zugang zu einem Segment des internen Netzwerks, das die Verwaltungssoftware für das Cold-Custody-System hostet.

**Ablauf des Vorfalls:**

| Zeit | Ereignis |
|---|---|
| 09.01.2026, 02:17 | SIEM-Alarm: ungewöhnlicher Zugriff VPN-Gateway |
| 09.01.2026, 02:45 | SOC (Schichtbetrieb) stuft als False Positive ein; keine Eskalation |
| 09.01.2026, 08:10 | Ransomware-Deployment entdeckt; 14 Server verschlüsselt |
| 09.01.2026, 08:30 | CISO Magnus Thorvaldsson informiert; IT-Notfall Stufe 2 ausgerufen |
| 09.01.2026, 10:00 | COO Marc Vellbruck informiert |
| 09.01.2026, 13:00 | Vollständige Vorstandsinfo; Isolierung infizierter Segmente |
| 09.01.2026, 16:00 | Forensik-Team extern mandatiert (CyberTrust GmbH, Frankfurt) |
| 10.-12.01.2026 | Forensische Analyse und Eindämmungsmaßnahmen |
| 13.01.2026, 14:32 | BaFin-Meldung über BAIT-Meldeportal |

---

## BAIT-Meldepflicht und Fristversäumnis

**Rechtsgrundlage:** BAIT 2024, Tz. 55: "Institute haben wesentliche IT-Sicherheitsvorfälle der Aufsicht unverzüglich anzuzeigen."

Die BaFin-Verwaltungspraxis definiert "unverzüglich" unter Rückgriff auf § 121 BGB analog als "ohne schuldhaftes Zögern, d.h. spätestens 24 Stunden nach Kenntniserlangung eines wesentlichen IT-Sicherheitsvorfalls." Zusätzlich verweist Tz. 55 BAIT auf die EBA-Leitlinien zu ICT- und Sicherheitsrisikomanagement (EBA/GL/2019/04), die eine Erstmeldung innerhalb von 4 Stunden nach Klassifizierung als wesentlich vorsehen.

**Sachverhaltsanalyse:**
- Kenntniserlangung für BAIT-Zwecke: spätestens 9. Januar 2026, 08:30 Uhr (CISO informiert).
- Meldung erfolgte: 13. Januar 2026, 14:32 Uhr.
- Verzug: 78 Stunden nach Pflichtbeginn (CISO-Kenntniserlangung), 30 Stunden nach Vollständiger-Vorstandskenntnis.

Der Meldungsverzug ist schwerwiegend. Das Institut beruft sich auf die laufende forensische Analyse, die abgewartet werden sollte, um der BaFin einen vollständigen Sachverhalt zu melden. Dieses Argument ist aufsichtsrechtlich schwach, da BAIT Tz. 55 ausdrücklich eine Erstmeldung mit den zum Zeitpunkt bekannten Informationen und Folgemeldungen bei fortschreitender Aufklärung vorsieht.

---

## Schadensumfang

- 14 Server des Verwaltungsnetzwerks verschlüsselt (keine Hot-Wallet-Systeme betroffen)
- Kundenfonds zu keinem Zeitpunkt gefährdet (Cold-Custody physisch getrennt)
- Produktionsausfall MPC-Signing-Service: 18 Stunden (9./10. Januar 2026)
- Keine Datenabrufanfragen von Kunden unerfüllt geblieben
- Forensik identifizierte: Angreifer hatten keinen Zugriff auf private Schlüssel
- Lösegeldforderung: 35 Bitcoin; Zahlung verweigert; Daten aus Backup wiederhergestellt

---

## Folgemaßnahmen (nach Vorfall)

1. Notfall-Patch FortiGate VPN-Gateway (10. Januar 2026, abgeschlossen)
2. Netzwerksegmentierung verschärft; Produktions- und Verwaltungsnetz strikter getrennt
3. SOC-Eskalationsprozesse überarbeitet; neues Runbook "IT-Notfall Stufe 1-3" erlassen
4. BAIT-Meldung nachgeholt (13. Januar 2026)
5. Nachträgliche Meldung auch an BSI nach BSIG (erfolgte parallel)

---

## Bewertung durch BaFin-Prüfer

Im Prüfungsgespräch vom 5. Mai 2026 qualifizierte Prüferin Dr. Kösters den Meldungsverzug als "schwerwiegende Pflichtverletzung nach BAIT Tz. 55", die isoliert ein Bußgeld nach § 56 GwG (sofern als Aufsichtsrechtsverletzung behandelt) oder eine Anordnung nach § 25a KWG rechtfertigen könne. Die Kanzlei bereitet eine Entlastungsargumentation vor, die auf die erstmalige Klassifizierungsunsicherheit und den bereits abgeschlossenen Remediation-Status abstellt.

**Vgl.:** 17-sanktionsrahmen-bussgeld-untersagung.md, 13-stellungnahme-vorstand-thalvenia.md
