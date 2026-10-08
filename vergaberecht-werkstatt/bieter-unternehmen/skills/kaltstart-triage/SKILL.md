---
name: kaltstart-triage
description: 'Verdichtet eine vom Master-Orchestrator bereits inventarisierte Bieterakte zu Rolle, Ziel, Fristen, LV-Formaten, Angebotsrisiken, Rechtsschutzbedarf und nächstem Fachskill. Nicht für rohe Ordner oder ZIP-Dateien; einzelne Dokumente übernimmt der Workflow-Kaltstart.'
---

# Bieter-Triage nach Erstinventur

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->

## Aktivierung

Dieser Skill folgt auf eine dokumentierte Erstinventur durch den Master-Orchestrator. Er ist nicht der Einstieg für rohe Ordner oder ZIP-Dateien. Ein einzelnes Dokument oder eine konkrete Frage übernimmt `workflow-kaltstart-und-routing`. Aus der bereits geordneten Akte wird genau der nächste Fachskill geladen, dessen Voraussetzungen erfüllt sind.

## Aktenstart

1. Dateien nach Format, Änderungsdatum, Absender, Verfahrensbezug und Lesbarkeit inventarisieren.
2. Leitdokumente erkennen: Bekanntmachung, Bewerbungsbedingungen, Leistungsbeschreibung, LV, Vertragsentwurf, Formblätter, Bieterfragen, Angebot, § 134-Information, Rüge, VK- oder OLG-Dokument.
3. GAEB, XML, Excel, PDF, E-Mail, Office- und Portalexporte in einer Dokumentenmatrix verknüpfen; Originale nicht überschreiben.
4. Widersprüche, Dubletten, fehlende Anlagen, unlesbare Scans und technische Rückgabeformate kennzeichnen.

## Entscheidungsweichen

| Weiche | festzustellende Tatsache | Folge |
|---|---|---|
| Rolle | Bewerber, Bieter, Bestbieter, ausgeschlossener Bieter, Bietergemeinschaft oder Nachunternehmer | Perspektive und Beweisbedarf |
| Stand | vor Teilnahme, Angebotsphase, Aufklärung, Wertung, § 134, Rüge, VK oder OLG | zulässiger nächster Schritt |
| Frist | Angebotsfrist, Kenntnis, Nichtabhilfe, Wartefrist, Zustellung | konkrete Kalenderfrist mit Beleg |
| Ziel | teilnehmen, liefern, Qualitätsvorteil zeigen, Zuschlag sichern, Fehler korrigieren oder angreifen | Output und Fachskill |
| Format | GAEB, XML, Excel, PDF, Plattformmaske oder Signatur | Import-, Validierungs- und Rückgabepfad |
| Risiko | Ausschluss, fehlender Nachweis, Preisaufklärung, schlechtere Qualitätswertung oder Zuschlag | Sofortpriorität |

## Automatisches Routing

| Aktenbefund | Fachskill | erstes Arbeitsprodukt |
|---|---|---|
| neue Vergabeunterlagen | `02-vergabeunterlagen-pruefen` | Pflichten-, Fristen- und Risikomatrix |
| Teilnahmeantrag oder Angebot | `angebot-in-vorgegebenem-format-erstellen` | Aufgabenplan und Compliance-Matrix |
| strukturierte oder alte Datenformate | `legacy-systeme-integration` | Import-, Mapping-, Prüf- und Exportplan |
| Qualitäts- oder Geschwindigkeitsvorteil | `qualitaetsvorsprung-nachweisen` | belegte Preis-Qualitäts-Argumentation |
| Eignungsfrage oder Ausschluss | `eignungspruefung` | Kriteriums-, Nachweis- und Rechtsfolgenmatrix |
| Fehler vor Zuschlag | `ruege-vor-zuschlag` | Rügeuhr und konkreter Abhilfeentwurf |
| Nichtabhilfe oder akuter Zuschlag | `vergabe-nachpruefung-aussicht` | Zulässigkeits-, Beleg- und Go-/Stop-Memo |
| Erstantrag bei der VK | `nachpruefungsantrag-vk` | vollständige Antragsschrift und Anlagenplan |
| laufendes VK-Verfahren | `nachpruefungsverfahren-vk` | Streitdashboard und nächster Schriftsatz |
| VK-Beschluss | `25-sofortige-beschwerde-olg-paragraf-171` | zugleich begründete OLG-Beschwerde |
| Einigungsfenster vor der VK | `vertiefung-vk-aufklaerung-vergleich` | rechtmäßiger Vergleichs- und Vollzugsplan |

Bei mehreren Treffern wird nur die notwendige Kette aktiviert. Beispiel: Unterlagenprüfung vor Angebotsentwurf; Datenformatprüfung vor Rückexport; Erfolgsaussicht vor Nachprüfungsantrag.

## Rechtsstands-Sofortcheck

- § 160 Abs. 3 GWB wird für jeden behaupteten Verstoß einzeln geprüft.
- § 134 Abs. 2 GWB richtet sich nach Absendung und Versandweg.
- § 169 Abs. 1 GWB beginnt erst mit Unterrichtung des Auftraggebers durch die Vergabekammer.
- Vor einer Beschwerde wird nach § 187 Abs. 2 GWB der Verfahrensbeginn ermittelt. Nur für ab 1. Juli 2026 begonnene Verfahren gelten die neuen §§ 172 und 173 GWB; Altverfahren einschließlich Rechtsmitteln folgen der bei Einleitung geltenden Fassung.
- Unterhalb der Schwellenwerte werden Bundesland, Auftraggebertyp und Sonderrechtsweg live bestimmt; ein VK-Weg wird nicht unterstellt.

## Erste Antwort

```text
Erkannt
[Vergabe, Rolle, Verfahrensstand und Leitdokumente]

Frist zuerst
[Datum, Rechenweg und Beleg oder klar bezeichnete Lücke]

Risiko und Ziel
[höchstes Ausschluss-, Angebots- oder Zuschlagsrisiko; gewünschtes Ergebnis]

Aktivierter Arbeitsweg
[Fachskill, Grund und sofort erzeugter Output]

Fehlt noch
[höchstens drei entscheidungserhebliche Unterlagen oder Fragen]
```

## Qualitätsgate

Keine generische Uploadbestätigung, keine Liste aller Skills und kein langes Interview. Eine Frist ohne Originalanker bleibt offen; eine Entscheidung ohne Quelle bleibt Prüfpunkt; ein Dateiformat ohne Rückgabetest bleibt technisch nicht freigegeben. Die Antwort endet mit einem bereits nutzbaren Arbeitsprodukt, nicht nur mit einem Vorschlag.
