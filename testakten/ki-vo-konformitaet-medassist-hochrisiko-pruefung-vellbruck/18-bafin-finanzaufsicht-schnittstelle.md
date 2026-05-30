# Aktenstück 18 — BaFin-Schnittstelle: Finanzaufsicht und Datenschutz-Berührungspunkte

**Aktenzeichen:** 2026-V-0427  
**Erstellt:** 26.04.2026  
**Bearbeitung:** RA Dr. Mark Roosendaal  
**Rechtsgrundlage:** KI-VoDG § 5 (BaFin-Zuständigkeit Finanzsektor); DSGVO Art. 9, 35; BfDI Az. 13-3120/004#0117

---

## 1. BaFin-Zuständigkeit im KI-VO-Kontext

Gemäß § 5 Abs. 2 KI-VoDG ist die Bundesanstalt für Finanzdienstleistungsaufsicht (BaFin) die zuständige Marktüberwachungsbehörde für KI-Systeme im Anwendungsbereich des Kreditwesengesetzes (KWG), der Versicherungsaufsicht (VAG) und verwandter Finanzmarktregulierung. MedAssist AI GmbH ist kein Finanzdienstleister; MedAssist v4 hat keine originäre Finanzsektoranwendung.

**Direkter BaFin-Bezug besteht nicht.** Das vorliegende Aktenstück dokumentiert jedoch zwei Berührungspunkte, die BaFin-relevante Aspekte tangieren:

---

## 2. D&O-Versicherung: BaFin-Aufsicht über Allianz SE

Die Kündigung der D&O-Police der Allianz SE (Schreiben 01.03.2026) ist versicherungsvertragsrechtlich relevant. Die Allianz SE unterliegt der Aufsicht durch die BaFin (§ 1 Abs. 1 Nr. 1 VAG). Sofern die Kündigung als Reaktion auf ein regulatorisches Verfahren (BNetzA-Marktüberwachung) erfolgt, stellt sich die Frage, ob ein Wettbewerbs- oder Aufsichtsrecht-Problem besteht.

**Einschätzung:** Die Kündigung der D&O-Versicherung ist privatrechtlich zulässig (§ 314 BGB, außerordentliche Kündigung bei schwerwiegender Pflichtverletzung). Eine BaFin-Intervention ist nicht zu erwarten. Die Kündigung entfaltet jedoch erheblichen Druck auf den Vorstand der MedAssist AI GmbH: Ohne D&O-Schutz haften CEO Dr. Vogelkamp und CTO Krishnamurthy persönlich für Schäden aus KI-VO-Verstößen (§ 43 GmbHG i.V.m. § 823 BGB). Dies verstärkt die Motivation zur schnellen Konformitätsherstellung.

**Empfehlung:** Erneute Verhandlung mit Allianz SE nach Vorlage des Handlungsplans und Nachweis der eingeleiteten Maßnahmen (insbesondere Quittierungsschritt-Rollout). Parallel: Marktabfrage alternativer D&O-Versicherer im KI-Bereich (z.B. AXA XL, Zurich).

---

## 3. BfDI: DPIA und Datenschutz-Berührungspunkte

### 3.1 BfDI-Anforderung (Az. 13-3120/004#0117)

Die Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI) hat mit Schreiben vom 15.02.2026 eine Datenschutz-Folgenabschätzung (DPIA) nach Art. 35 DSGVO angefordert. Die BfDI begründet die Anforderung mit:

- Systematische Verarbeitung von Gesundheitsdaten (Art. 9 Abs. 1 DSGVO) in großem Maßstab (18 Krankenhäuser, täglich ca. 3.200 Notrufe)
- Automatisierte Entscheidungsunterstützung mit potenzieller Wirkung auf Betroffene (Patienten), Art. 22 DSGVO
- Verarbeitung von Daten besonderer Kategorien ohne ausreichend dokumentierte Rechtsgrundlage

### 3.2 Art. 35 DSGVO — Pflicht zur DPIA

Art. 35 Abs. 3 lit. a DSGVO: Eine DPIA ist obligatorisch bei „systematischer und umfangreicher Verarbeitung besonderer Kategorien von Daten gemäß Art. 9". Dies ist hier eindeutig gegeben.

Die DPIA hätte vor Inbetriebnahme von MedAssist v4 durchgeführt werden müssen. Das Versäumnis begründet einen Verstoß gegen Art. 35 DSGVO, für den die BfDI Bußgelder nach Art. 83 Abs. 4 DSGVO (bis 10 Mio. EUR oder 2 % des weltweiten Jahresumsatzes) verhängen kann.

### 3.3 DPIA-Inhalte (Art. 35 Abs. 7 DSGVO)

Die DPIA muss enthalten:
- Systematische Beschreibung der Verarbeitungsvorgänge und Verarbeitungszwecke
- Bewertung der Notwendigkeit und Verhältnismäßigkeit
- Bewertung der Risiken für die Rechte und Freiheiten der betroffenen Personen
- Vorgesehene Abhilfemaßnahmen, Sicherheitsmaßnahmen und Garantien

**Besonderheit KI:** Für KI-Systeme empfiehlt das European Data Protection Board (EDPB), in der DPIA auch das Risiko algorithmischer Diskriminierung (Bias) zu adressieren. Dies schlägt die Brücke zu Art. 10 KI-VO (s. Aktenstück 05).

---

## 4. Art. 22 DSGVO — Automatisierte Einzelentscheidungen

Art. 22 Abs. 1 DSGVO: Personen haben das Recht, nicht einer ausschließlich automatisierten Entscheidung unterworfen zu werden, die ihnen gegenüber rechtliche Wirkung entfaltet oder sie in ähnlicher Weise erheblich beeinträchtigt. Im Notfalldispositionskontext: Wird die Ressourcenzuweisung durch MedAssist v4 faktisch ohne menschliche Prüfung übernommen (was in 14 Kliniken der Fall ist), kann dies als „ausschließlich automatisierte" Entscheidung qualifiziert werden.

**Handlungsempfehlung:** Der Roll-out des Pflicht-Quittierungsschritts (Art. 14 KI-VO) löst zugleich die Art. 22 DSGVO-Problematik. Die DPIA muss diesen Zusammenhang explizit dokumentieren.

---

## 5. Handlungsempfehlungen

| Maßnahme | Frist | Verantwortlich |
|---|---|---|
| DPIA erstellen und BfDI vorlegen | 01.05.2026 | Dr. Roosendaal (federführend) |
| Allianz SE: Verhandlung D&O-Verlängerung nach Handlungsplan-Vorlage | 15.05.2026 | CEO Dr. Vogelkamp |
| Art. 22 DSGVO-Analyse in DPIA integrieren | 01.05.2026 | Dr. Roosendaal |
| Rechtsgrundlagen-Prüfung AVV 18 Kliniken (Art. 9 DSGVO) | 31.05.2026 | Dr. Roosendaal |

---

*Heidelberg, 26.04.2026*  
*RA Dr. Mark Roosendaal — Az. 2026-V-0427*
