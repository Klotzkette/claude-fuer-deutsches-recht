---
name: idw-s6-integrierte-sanierungsplanung
description: "Für Integrierte Sanierungsplanung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

<!-- decimal-anchor --> <a id="integrierte-sanierungsplanung"></a>

# 1. Integrierte Sanierungsplanung

<!-- decimal-anchor --> <a id="fachkern-integrierte-sanierungsplanung"></a>

## 1.1. Fachkern: Integrierte Sanierungsplanung
- **Normen-/Quellenanker:** InsO §§ 17, 18, 19, 15a, StaRUG-Früherkennung, IDW-S-6-/Planungslogik, 3-Wochen- und 13-Wochen-Forecast, Zahlungsstatus und Fortbestehensprognose.
- **Entscheidende Weiche:** Trenne fällige Verbindlichkeiten, liquide Mittel, harte Zahlungszusagen, Planannahmen, Quote/Lücke, Organpflicht und Dokumentationsspur.

<!-- decimal-anchor --> <a id="wann-starten"></a>

## 1.2. Wann starten?

- 13-Wochen-Plan ist erstellt, aber Bank verlangt Sanierungskonzept.
- Fortbestehensprognose nach § 19 InsO soll dokumentiert werden.
- StaRUG-, Schutzschirm-, Eigenverwaltungs- oder Insolvenzplanroute steht im Raum.
- Maßnahmenliste existiert, aber ihre finanzielle Wirkung ist unklar.
- Kleine Gesellschaft hat nur BWA, OPOS und Bankauszüge; trotzdem braucht es eine belastbare Planung.

<!-- decimal-anchor --> <a id="eingangsrouting"></a>

## 1.3. Eingangsrouting

Wenn nur kurzfristige Zahlungsunfähigkeit geprüft wird, zuerst `liquiditaetsvorschau-3wochen` oder `liquiditaetsvorschau-insolvenzrechtlich`. Wenn daraus ein Sanierungskonzept, eine Bankunterlage oder eine Fortbestehensprognose werden soll, anschließend diesen Skill nutzen.

<!-- decimal-anchor --> <a id="planungsarchitektur"></a>

## 1.4. Planungsarchitektur

Baue die Planung in vier Ebenen:

1. **Direkte Liquiditätsplanung:** Einzahlungen, Auszahlungen, Linien, freie Liquidität, Engpasswochen.
2. **GuV-Planung:** Umsatz, Rohertrag, Personal, Fixkosten, Zinsen, Steuern, Ergebnis.
3. **Bilanzplanung:** Working Capital, Anlagevermögen, Rückstellungen, Finanzverbindlichkeiten, Eigenkapital.
4. **Maßnahmen- und Annahmenlog:** Jede wesentliche Veränderung mit Quelle, Verantwortlichem, Timing und Risiko.

Alle Ebenen müssen rechnerisch zusammenpassen. Wenn sie nicht passen, ist das Ergebnis eine Lückenliste, nicht eine geschönte Planung.

<!-- decimal-anchor --> <a id="mindesttiefe"></a>

## 1.5. Mindesttiefe

- Für akute Krisen: wöchentliche Liquidität für 13 Wochen.
- Für Fortbestehensprognose: mindestens 12 Monate mit belastbarer Liquiditätsreichweite.
- Für Sanierungskonzept: laufendes und folgendes Planjahr regelmäßig monatlich; spätere Jahre können verdichtet werden, wenn die Brücken transparent bleiben.
- Für kleinere Unternehmen: weniger Kontenzeilen sind zulässig, aber GuV, Bilanz und Liquidität müssen trotzdem verknüpft sein.

<!-- decimal-anchor --> <a id="maßnahmen-brücke"></a>

## 1.6. Maßnahmen-Brücke

Lege für jede Maßnahme einen Datensatz an:

```yaml
massnahme:
 titel: "[z. B. Standortkonsolidierung / Bankstundung / Kapitalzufuhr]"
 krisenursache: "[welche Ursache wird adressiert?]"
 status: "verbindlich | verhandelt | plausibel | ungeklärt | nicht tragfähig"
 guv-effekt:
 umsatz: "[EUR / Prozent / Monat]"
 kosten: "[EUR / Monat]"
 zinsen_steuern: "[EUR / Monat]"
 liquiditaets-effekt:
 einmalig: "[EUR, Datum]"
 laufend: "[EUR, ab Datum]"
 vorfinanzierungsbedarf: "[EUR]"
 bilanz-effekt:
 eigenkapital: "[EUR]"
 verbindlichkeiten: "[EUR]"
 working_capital: "[EUR]"
 voraussetzungen:
 - "[Beschluss, Vertrag, Finanzierung, Zustimmung]"
 nachweise:
 - "[Datei / Vertrag / Beschluss / Kontoauszug]"
 risiko:
 sensitivitaet: "[was passiert bei Verzug oder Teilwirkung?]"
```

<!-- decimal-anchor --> <a id="sanierungsfähigkeits-ampel"></a>

## 1.7. Sanierungsfähigkeits-Ampel

Bewerte am Ende:

| Ampel | Bedeutung | Konsequenz |
|---|---|---|
| Grün | Liquidität, Ertrag, Bilanz und Maßnahmen tragen auch in plausibler Sensitivität. | Planung kann als Arbeitsstand für Konzept, Bank oder Planroute genutzt werden. |
| Gelb | Basisfall trägt, aber eine tragende Annahme oder Maßnahme ist nicht belegt. | Conditional Go; Datenanforderung und Nachweisfrist ausgeben. |
| Rot | Planung kippt bei naheliegender Abweichung oder beseitigt Krisenursachen nicht. | Keine positive Sanierungsfähigkeit ausgeben; Eskalation zu Insolvenz-/Restrukturierungsberatung. |

<!-- decimal-anchor --> <a id="annahmenlog"></a>

## 1.8. Annahmenlog

Jede wesentliche Annahme braucht:

- Quelle: historische Daten, Vertrag, Auftrag, Managementangabe, Marktbeleg, Steuerbescheid, Bankzusage.
- Plausibilisierung: Vergangenheit, Branchenlogik, Kapazität, Preis-/Mengenbrücke, Gegenparteirisiko.
- Sensitivität: Best/Base/Worst oder mindestens Base/Downside.
- Verantwortlicher: wer aktualisiert und wer entscheidet?
- Wiedervorlage: wann wird die Annahme neu geprüft?

<!-- decimal-anchor --> <a id="spezielle-prüfbereiche"></a>

## 1.9. Spezielle Prüfbereiche

- **Working Capital:** Zahlungsziele, Forderungsausfall, Vorratsaufbau, Lieferantenkredite.
- **Finanzierung:** Linienverfügbarkeit, Kündigungsrechte, Covenants, Tilgungsprofil, Sicherheiten.
- **Steuern und Sozialversicherung:** Fälligkeiten, Rückstände, Stundung, Nebenforderungen.
- **Personal:** Abbaukosten, Kündigungsfristen, Betriebsrat, Insolvenzgeldzeitraum.
- **Investitionen:** Erhaltungs-CapEx nicht mit Null ansetzen, wenn Betrieb sonst ausfällt.
- **Cyber/IT/ESG:** nur dort vertiefen, wo sie für Betrieb, Markt, Finanzierung oder Haftung wesentlich sind.

<!-- decimal-anchor --> <a id="ausgabe"></a>

## 1.10. Ausgabe

Liefer standardmäßig:

1. **Planungsanforderung** mit Datenliste und Priorität.
2. **Annahmenlog** als Tabelle.
3. **Maßnahmen-Brücke** zwischen Maßnahme, GuV, Bilanz und Liquidität.
4. **Sanierungsplanungs-Ampel** mit Gründen und Stoppern.
5. **Nächster Arbeitsschritt:** Liquiditätsplan aktualisieren, Planbilanz bauen, Maßnahmen belegen, oder insolvenzrechtlich eskalieren.

<!-- decimal-anchor --> <a id="typische-fehler"></a>

## 1.11. Typische Fehler

- Liquiditätsvorschau wird als vollständige Sanierungsplanung verkauft.
- Maßnahmen werden doppelt gezählt: einmal in GuV, einmal im Cashflow.
- Steuern aus Sanierungsmaßnahmen fehlen.
- Working-Capital-Effekt des Wachstums wird ignoriert.
- Planjahr schließt liquiditätsseitig, aber Bilanz stimmt nicht.
- Gesellschafter- oder Bankbeitrag wird ohne belastbare Tatsachen zu Leistungsfähigkeit, Leistungsbereitschaft, Betrag, Zeitpunkt und Bedingungen angesetzt. Für die §-19-Fortbestehensprognose ist ein einklagbarer Anspruch nicht stets zwingend; die überwiegende Wahrscheinlichkeit des Beitrags und des Gesamtkonzepts ist nach BGH, Urteil vom 13.07.2021 – II ZR 84/20, Rn. 77–85, zu begründen. Die strengere kurzfristige Mittelverfügbarkeit und die Aktivierung im Überschuldungsstatus bleiben gesonderte Fragen.
- Kleine Unternehmen werden zu grob geplant, obwohl einzelne Großkunden oder Schlüsselpersonen das Risiko treiben.
