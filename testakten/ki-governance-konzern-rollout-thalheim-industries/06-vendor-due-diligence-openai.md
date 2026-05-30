# Vendor Due Diligence — OpenAI Ireland Ltd. / CodeAssist

**Aktenzeichen:** TI-KI-2026-011
**Dokumentversion:** 1.1
**Erstellungsdatum:** 05. Februar 2026
**Verfasser:** Marcus Petersen (CDO); Annegret Kühnhausen (CCO)
**Status:** Offene Punkte; Nachforderung an OpenAI Ireland Ltd. verschickt 15.02.2026

---

## 1. Hintergrund

Thalheim Industries SE setzt im Bereich Software-Entwicklung das Tool **CodeAssist** ein, das auf dem Sprachmodell GPT-4o von OpenAI Ireland Ltd. basiert. Der Vertrag besteht seit Juli 2024 (Enterprise-Lizenz, Vertragsnummer OAI-ENT-2024-TI-0892). CodeAssist ist im KI-Inventar als System mit begrenztem Risiko (GPAI-Modell, Art. 51 ff. KI-VO) klassifiziert.

Als Betreiber (Deployer) nach Art. 3 Nr. 4 KI-VO ist Thalheim Industries SE verpflichtet, sicherzustellen, dass das eingesetzte KI-System den Anforderungen der KI-VO entspricht. OpenAI Ireland Ltd. ist als Anbieter (Provider) des Basismodells nach Art. 53 KI-VO verpflichtet, folgende Pflichten zu erfüllen:
- Erstellung und Pflege technischer Dokumentation (Art. 53 Abs. 1 lit. a KI-VO);
- Einhaltung geltenden Urheberrechts (Art. 53 Abs. 1 lit. c KI-VO);
- Bereitstellung einer Zusammenfassung der Trainingsdaten (Art. 53 Abs. 1 lit. d KI-VO);
- Für Systeme mit systemischem Risiko: Meldepflichten, Adversarial Tests (Art. 55 KI-VO).

---

## 2. Prüfgegenstand

Im Rahmen der Due Diligence wurden folgende Themenbereiche untersucht:

| Prüfbereich | Prüffrage | Ergebnis |
|---|---|---|
| Technische Dokumentation (Art. 11 / Art. 53 KI-VO) | Vollständige technische Dok. für CodeAssist vorgelegt? | **Nicht vollständig** |
| Datenschutz / Auftragsverarbeitung | AVV (DSGVO Art. 28) abgeschlossen? | Ja — OAI-DPA-2024-TI |
| Drittlandübermittlung | Verarbeitung in der EU sichergestellt (EEA-Verarbeitungsoption)? | Ja (EU-Data-Residency aktiv) |
| Nutzungsbedingungen / AUP | Entspricht Nutzung den OpenAI-Acceptable-Use-Policies? | Ja — geprüft |
| Incident Response | OpenAI-Sicherheitsvorfallmeldungen an Thalheim klar geregelt? | Teilweise — SLA unklar |
| KI-VO-Compliance-Seite OpenAI | Liegt produktspezifische EU-AI-Act-Konformitätserklärung vor? | **Nicht produktspezifisch** |
| Urheberrecht / IP | Code-Output-IP-Regelung vertraglich klar? | Ja — Vertrag §§ 6–8 |
| Cybersicherheit | SOC 2 Type II vorliegend? | Ja (aktuell, gültig bis 11/2026) |

---

## 3. Festgestellte Mängel

### Mangel 1 — Fehlende produktspezifische technische Dokumentation

OpenAI hat auf Thalheims Anfrage (Schreiben CDO Petersen, 20.01.2026) lediglich auf die allgemeine EU-AI-Act-Compliance-Seite (https://openai.com/eu-ai-act) verwiesen. Diese enthält keine produktspezifischen Informationen zu CodeAssist als Deployment-Szenario für Thalheim. Insbesondere fehlen:

- Angaben zu den Trainings- und Testdaten-Parametern (Art. 53 Abs. 1 lit. d KI-VO);
- Dokumentation der implementierten Sicherheitsmechanismen;
- Angaben zu bekannten Schwächen des Modells (Known Limitations, Bias-Disclosure).

Die Anforderungen nach Art. 53 Abs. 1 lit. a und d KI-VO sind für Anbieter von Allzweck-KI-Modellen (GPAI-Modelle) verbindlich. OpenAI Ireland Ltd. ist als Anbieter des GPT-4o-Modells ein GPAI-Modell-Anbieter im Sinne von Art. 3 Nr. 63 KI-VO. Die Tatsache, dass ein generischer Compliance-Link bereitgestellt wird, genügt den Anforderungen nicht.

**Bewertung:** Kritischer Mangel. Nachforderung erforderlich.

### Mangel 2 — Unklare SLA für Security-Incident-Meldungen

Der bestehende Vertrag (OAI-ENT-2024-TI-0892, Section 9) enthält keine spezifischen SLA-Klauseln zu den Fristen für Sicherheitsvorfallmeldungen, die KI-spezifische Risiken betreffen. Nach Art. 73 KI-VO sind Betreiber verpflichtet, schwerwiegende Vorfälle innerhalb von 15 Tagen (bei Todesfällen: sofort) an die nationale Marktüberwachungsbehörde zu melden. Dazu muss der Vendor unverzüglich informieren.

**Bewertung:** Mittlerer Mangel. Vertragsergänzung erforderlich.

---

## 4. Nachforderungsschreiben (zusammengefasst)

Mit Schreiben vom 15. Februar 2026 (CDO Petersen, Ref. TI-CDO-2026-0041) hat Thalheim OpenAI Ireland Ltd. folgende Unterlagen angefordert:

1. Produktspezifische technische Dokumentation für den Einsatz von GPT-4o in CodeAssist-Deployment-Szenarios nach Art. 53 KI-VO;
2. Zusammenfassung der Trainingsdatenbasis des eingesetzten Modells;
3. Disclosure bekannter Schwächen (Halluzinierungsrate, Bias-Kategorie);
4. Ergänzende Vereinbarung zu Sicherheitsvorfallmeldungen (Incident Notification SLA max. 24 h);
5. Klarstellung, ob GPT-4o als GPAI-Modell mit systemischem Risiko eingestuft ist (Art. 51 KI-VO).

**Antwortfrist:** 30. April 2026.

---

## 5. Handlungsempfehlungen

| Empfehlung | Priorität | Frist |
|---|---|---|
| Eskalation bei OpenAI auf Enterprise-Account-Manager-Ebene | Hoch | Sofort |
| Prüfung alternativer Vendor-Optionen für KI-Coding-Assistent (z. B. GitHub Copilot, Anthropic Claude) | Mittel | 30.06.2026 |
| Vertragsergänzung: Incident Notification SLA, EU-AI-Act-Klausel | Hoch | 30.04.2026 |
| Interne Nutzungsrichtlinie CodeAssist aktualisieren: keine personenbezogenen Daten, keine geheimen Informationen in Prompts | Hoch | 28.02.2026 ✓ (erledigt) |
| AI Literacy Schulung IT-Personal (Modul E) priorisieren | Mittel | 30.06.2026 |

---

## 6. Vendor-Risikobewertung (Gesamt)

| Kriterium | Bewertung | Begründung |
|---|---|---|
| Datenschutz-Compliance | Gut | AVV vorhanden, EEA-Residency aktiv |
| KI-VO-Dokumentation | **Unzureichend** | Keine produktspezifische Doku |
| Finanzielle Stabilität | Sehr gut | OpenAI valide Marktkapitalisierung |
| Vertragliche KI-VO-Klauseln | Ausbaubar | Nachverhandlung erforderlich |
| Cybersicherheit | Gut | SOC 2 Type II aktuell |
| **Gesamtrisiko** | **Mittel** | Doku-Mangel behebbar, aber fristkritisch |

---

*Aktenzeichen: TI-KI-2026-011. Verfasser: M. Petersen, A. Kühnhausen. Stand: März 2026.*
