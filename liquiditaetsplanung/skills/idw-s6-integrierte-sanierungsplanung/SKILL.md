---
name: idw-s6-integrierte-sanierungsplanung
description: "Verbindet Liquiditätsvorschau, GuV-Planung und Planbilanz zu einer Sanierungsplanung auf IDW-S-6-Niveau. Prüft Maßnahmenwirkung, Fortbestehensprognose, Sanierungsfähigkeit, Szenarien, Planungsannahmen, Belegregister, kleinere Unternehmen und Übergabe an Bank, Insolvenzverwalter oder Restrukturierungsberater. Output: Planungsanforderung, Annahmenlog, Maßnahmen-Brücke und Sanierungsplanungs-Ampel."
---

# Integrierte Sanierungsplanung

## Fachkern: Integrierte Sanierungsplanung
- **Normen-/Quellenanker:** InsO §§ 17, 18, 19, 15a, StaRUG-Früherkennung, IDW-S-6-/Planungslogik, 3-Wochen- und 13-Wochen-Forecast, Zahlungsstatus und Fortbestehensprognose.
- **Entscheidende Weiche:** Trenne fällige Verbindlichkeiten, liquide Mittel, harte Zahlungszusagen, Planannahmen, Quote/Lücke, Organpflicht und Dokumentationsspur.

## Aufgabe

Dieser Skill hebt eine Liquiditätsvorschau auf Sanierungskonzept-Niveau. Er prüft nicht nur, ob in den nächsten Wochen Geld reicht, sondern ob Maßnahmen, Ergebnisplanung, Bilanzplanung und Liquiditätsplanung zusammen ein konsistentes Bild ergeben.

Nutze ihn, wenn ein Unternehmen, eine Bank, ein Insolvenzverwalter, ein Sachwalter, ein Restrukturierungsberater oder ein Gericht nicht nur einen Cash-Forecast, sondern eine tragfähige Sanierungsplanung braucht.

## Wann starten?

- 13-Wochen-Plan ist erstellt, aber Bank verlangt Sanierungskonzept.
- Fortbestehensprognose nach § 19 InsO soll dokumentiert werden.
- StaRUG-, Schutzschirm-, Eigenverwaltungs- oder Insolvenzplanroute steht im Raum.
- Maßnahmenliste existiert, aber ihre finanzielle Wirkung ist unklar.
- Kleine Gesellschaft hat nur BWA, OPOS und Bankauszüge; trotzdem braucht es eine belastbare Planung.

## Eingangsrouting

Wenn nur kurzfristige Zahlungsunfähigkeit geprüft wird, zuerst `liquiditaetsvorschau-3wochen` oder `liquiditaetsvorschau-insolvenzrechtlich`. Wenn daraus ein Sanierungskonzept, eine Bankunterlage oder eine Fortbestehensprognose werden soll, anschließend diesen Skill nutzen.

## Planungsarchitektur

Baue die Planung in vier Ebenen:

1. **Direkte Liquiditätsplanung:** Einzahlungen, Auszahlungen, Linien, freie Liquidität, Engpasswochen.
2. **GuV-Planung:** Umsatz, Rohertrag, Personal, Fixkosten, Zinsen, Steuern, Ergebnis.
3. **Bilanzplanung:** Working Capital, Anlagevermögen, Rückstellungen, Finanzverbindlichkeiten, Eigenkapital.
4. **Maßnahmen- und Annahmenlog:** Jede wesentliche Veränderung mit Quelle, Verantwortlichem, Timing und Risiko.

Alle Ebenen müssen rechnerisch zusammenpassen. Wenn sie nicht passen, ist das Ergebnis eine Lückenliste, nicht eine geschönte Planung.

## Mindesttiefe

- Für akute Krisen: wöchentliche Liquidität für 13 Wochen.
- Für Fortbestehensprognose: mindestens 12 Monate mit belastbarer Liquiditätsreichweite.
- Für Sanierungskonzept: laufendes und folgendes Planjahr regelmäßig monatlich; spätere Jahre können verdichtet werden, wenn die Brücken transparent bleiben.
- Für kleinere Unternehmen: weniger Kontenzeilen sind zulässig, aber GuV, Bilanz und Liquidität müssen trotzdem verknüpft sein.

## Maßnahmen-Brücke

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

## Sanierungsfähigkeits-Ampel

Bewerte am Ende:

| Ampel | Bedeutung | Konsequenz |
|---|---|---|
| Grün | Liquidität, Ertrag, Bilanz und Maßnahmen tragen auch in plausibler Sensitivität. | Planung kann als Arbeitsstand für Konzept, Bank oder Planroute genutzt werden. |
| Gelb | Basisfall trägt, aber eine tragende Annahme oder Maßnahme ist nicht belegt. | Conditional Go; Datenanforderung und Nachweisfrist ausgeben. |
| Rot | Planung kippt bei naheliegender Abweichung oder beseitigt Krisenursachen nicht. | Keine positive Sanierungsfähigkeit ausgeben; Eskalation zu Insolvenz-/Restrukturierungsberatung. |

## Annahmenlog

Jede wesentliche Annahme braucht:

- Quelle: historische Daten, Vertrag, Auftrag, Managementangabe, Marktbeleg, Steuerbescheid, Bankzusage.
- Plausibilisierung: Vergangenheit, Branchenlogik, Kapazität, Preis-/Mengenbrücke, Gegenparteirisiko.
- Sensitivität: Best/Base/Worst oder mindestens Base/Downside.
- Verantwortlicher: wer aktualisiert und wer entscheidet?
- Wiedervorlage: wann wird die Annahme neu geprüft?

## Spezielle Prüfbereiche

- **Working Capital:** Zahlungsziele, Forderungsausfall, Vorratsaufbau, Lieferantenkredite.
- **Finanzierung:** Linienverfügbarkeit, Kündigungsrechte, Covenants, Tilgungsprofil, Sicherheiten.
- **Steuern und Sozialversicherung:** Fälligkeiten, Rückstände, Stundung, Nebenforderungen.
- **Personal:** Abbaukosten, Kündigungsfristen, Betriebsrat, Insolvenzgeldzeitraum.
- **Investitionen:** Erhaltungs-CapEx nicht mit Null ansetzen, wenn Betrieb sonst ausfällt.
- **Cyber/IT/ESG:** nur dort vertiefen, wo sie für Betrieb, Markt, Finanzierung oder Haftung wesentlich sind.

## Ausgabe

Liefer standardmäßig:

1. **Planungsanforderung** mit Datenliste und Priorität.
2. **Annahmenlog** als Tabelle.
3. **Maßnahmen-Brücke** zwischen Maßnahme, GuV, Bilanz und Liquidität.
4. **Sanierungsplanungs-Ampel** mit Gründen und Stoppern.
5. **Nächster Arbeitsschritt:** Liquiditätsplan aktualisieren, Planbilanz bauen, Maßnahmen belegen, oder insolvenzrechtlich eskalieren.

## Typische Fehler

- Liquiditätsvorschau wird als vollständige Sanierungsplanung verkauft.
- Maßnahmen werden doppelt gezählt: einmal in GuV, einmal im Cashflow.
- Steuern aus Sanierungsmaßnahmen fehlen.
- Working-Capital-Effekt des Wachstums wird ignoriert.
- Planjahr schließt liquiditätsseitig, aber Bilanz stimmt nicht.
- Gesellschafter- oder Bankbeitrag ist nicht verbindlich.
- Kleine Unternehmen werden zu grob geplant, obwohl einzelne Großkunden oder Schlüsselpersonen das Risiko treiben.

## Quellenregel

Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben. Berufsständische Standards als methodischen Maßstab verwenden, nicht als Zitierersatz.
