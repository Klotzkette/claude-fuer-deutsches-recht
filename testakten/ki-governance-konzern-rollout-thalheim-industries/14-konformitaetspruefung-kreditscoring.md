# Konformitätsprüfung CreditVision Score — Vorbereitende Analyse

**Aktenzeichen:** TI-KI-2026-015
**Dokumentversion:** 0.9 (Vorab-Analyse, Audit geplant Mai 2026)
**Erstellungsdatum:** 25. März 2026
**Verfasser:** Annegret Kühnhausen (CCO); Rolf Haselmann (Leiter Kundenfinanzierung)
**Externe Begleitung:** Kanzlei Borchmann Compliance

---

## 1. Gegenstand und Ausgangslage

Das Kreditscoring-Modul **CreditVision Score** (Vendor: CreditVision AG, Frankfurt am Main) ist als Hochrisiko-KI-System nach Art. 6 Abs. 2 i.V.m. Anhang III Nr. 5 lit. b KI-VO (https://dejure.org/gesetze/KIVO/6.html) klassifiziert. Es berechnet Bonitätsscores für Privat- und Gewerbekunden der Thalheim-Kundenfinanzierungseinheit und fließt in Kreditentscheidungen bei Investitionsgütern und Energieanlagen-Finanzierungen ein.

Die offene BaFin-Anfrage (GZ BJ 24-K 7102-2026/0012, eingegangen 10.03.2026, Antwortfrist 15.05.2026) hat die Konformitätsprüfung zu einem vorrangigen Compliance-Thema gemacht. Die vollständige interne Konformitätsbewertung durch Hagedorn & Partner ist für Mai/Juni 2026 geplant. Das vorliegende Dokument bereitet die Prüfung vor.

---

## 2. System-Steckbrief

| Merkmal | Inhalt |
|---|---|
| System | CreditVision Score v4.2 |
| Vendor | CreditVision AG, Mainzer Landstraße 220, 60326 Frankfurt |
| Vertrag | CV-ENT-2023-TI-0441 (seit 01.04.2023) |
| Einsatzbereich | Kundenfinanzierung Thalheim Industries SE |
| Entscheidungsgewicht | Score fließt zu 60 % in Kreditentscheidung ein; 40 % Sachbearbeiter-Urteil |
| Kreditvolumen p.a. | ca. 340 Mio. EUR (Neuabschlüsse) |
| Betroffene Personen | Ca. 1.200 Neukunden p.a. (natürliche Personen und Unternehmer) |
| Datenbasis | Eigenangaben Kunden, Schufa-Score, Kontoauszüge (optionaler PSD2-Zugang), Branchendaten |

---

## 3. Prüfung Art. 22 DSGVO

**Sachverhalt:** CreditVision Score unterstützt Kreditentscheidungen, die erhebliche Rechtsfolgen für Kunden haben (Kreditbewilligung oder -ablehnung). Dies fällt unter Art. 22 Abs. 1 DSGVO (https://dejure.org/gesetze/DSGVO/22.html), wenn die Entscheidung ausschließlich oder überwiegend auf automatisierter Verarbeitung beruht.

**Analyse:**
- Bei einem Score-Gewicht von 60 % liegt noch keine „ausschließlich automatisierte" Entscheidung vor, wenn der Sachbearbeiter aktiv entscheidet.
- Kritisch: In der Praxis folgen Sachbearbeiter dem Score in 94 % der Fälle, was de facto einer automatisierten Entscheidung nahekommt (vgl. EuGH, Urteil vom 07.12.2023, Rs. C-634/21, „SCHUFA Holding AG" — obiter dicta zur funktionalen Automationsqualität).
- Empfehlung: Sachbearbeiterprozess stärken; aktives Dokumentationserfordernis bei Abweichungen nach oben und unten.

**Maßnahmen Art. 22 DSGVO:**
- Datenschutzhinweis überarbeiten: Kunden über Kreditscoring informieren (Art. 13 DSGVO).
- Erklärungsrecht dokumentieren: Kunden haben Recht auf Erläuterung der Score-Faktoren.
- Widerspruchsrecht verankern: Kunden können menschliche Überprüfung verlangen.

---

## 4. Vorprüfung der Hochrisiko-Pflichten

| Pflicht | Rechtsgrundlage | Vorabeinschätzung | Handlungsbedarf |
|---|---|---|---|
| Risikomanagementsystem | Art. 9 KI-VO | Vorhanden (CreditVision-intern) | Thalheim-spezifische Ergänzung |
| Bias-Tests | Art. 9 Abs. 7 KI-VO | Unklar — CreditVision keine Aussage | **Nachforderung dringend** |
| Daten-Governance | Art. 10 KI-VO | Teilweise dokumentiert | Herkunft Schufa-Daten klären |
| Technische Dokumentation | Art. 11 KI-VO | Teilweise geliefert | Nachforderung läuft |
| Protokollierung | Art. 12 KI-VO | Log-Daten vorhanden | Aufbewahrungsfrist prüfen |
| Gebrauchsanweisung | Art. 13 KI-VO | Vorhanden (DE, EN) | Ausreichend |
| Menschliche Aufsicht | Art. 14 KI-VO | Prozessual verankert | Dokumentationspraxis verbessern |
| Genauigkeit / Robustheit | Art. 15 KI-VO | Keine unabhängige Prüfung | Unabhängiges Testing planen |
| Cybersicherheit | Art. 15 KI-VO | ISO 27001 CreditVision AG | Zertifikat anfordern |

---

## 5. Inhalt der BaFin-Stellungnahme (Entwurf)

*Für BaFin GZ BJ 24-K 7102-2026/0012, Antwortfrist 15.05.2026:*

**Zu Frage 1 — Art. 22 DSGVO:** Thalheim erklärt, dass CreditVision Score Entscheidungsunterstützungs-, kein Entscheidungssystem ist. Die abschließende Kreditentscheidung trifft ein qualifizierter Sachbearbeiter. Die Informationspflichten nach Art. 13 DSGVO werden seit [Datum] durch den aktualisierten Datenschutzhinweis erfüllt. Das Widerspruchsrecht nach Art. 22 Abs. 3 DSGVO ist im Kundenprozess verankert.

**Zu Frage 2 — Art. 43 Abs. 2 KI-VO:** Die vollständige interne Konformitätsbewertung für CreditVision Score ist für Mai/Juni 2026 geplant und wird von WPG Hagedorn & Partner begleitet. Der Abschlussbericht wird der BaFin nach Fertigstellung (geplant 31.07.2026) übermittelt. Thalheim verpflichtet sich, bis dahin den Status monatlich zu berichten.

---

## 6. Risikobewertung Gesamtsystem

| Risiko | Bewertung | Maßnahme |
|---|---|---|
| Diskriminierung in Kreditentscheidungen | Mittel | Bias-Tests CreditVision beauftragen |
| Art. 22 DSGVO-Verstoß | Mittel | Dokumentationsprozess stärken |
| Unvollständige Vendor-Dokumentation | Hoch | Nachforderung, Vertragsstrafe prüfen |
| BaFin-Sanktion | Niedrig (mit Stellungnahme) | Fristgerechte, vollständige Antwort |
| Reputationsrisiko | Niedrig bis mittel | Proaktive Kommunikation an BaFin |

---

*Aktenzeichen: TI-KI-2026-015. Verfasser: A. Kühnhausen, R. Haselmann. Stand: März 2026.*
